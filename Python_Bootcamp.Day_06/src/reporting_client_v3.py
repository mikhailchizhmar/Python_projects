import argparse
import grpc
import json
import spaceship_pb2
import spaceship_pb2_grpc
from pydantic import ValidationError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from schemas import Base, Spaceship as ORMSpaceship, Officer as ORMOfficer, spaceship_officers
import models as m

DATABASE_URL = "postgresql+psycopg2://newtonbe:password@localhost/spaceship_reports"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def save_spaceship(db, spaceship_data):
    officers_data = spaceship_data.pop('officers', [])
    spaceship = ORMSpaceship(**spaceship_data)
    db.add(spaceship)
    db.commit()
    db.refresh(spaceship)

    for officer_data in officers_data:
        officer = db.query(ORMOfficer).filter_by(**officer_data).first()
        if not officer:
            officer = ORMOfficer(**officer_data)
            db.add(officer)
            db.commit()
            db.refresh(officer)
        spaceship.officers.append(officer)

    db.commit()


def scan_coordinates(db, coordinates):
    coordinates = spaceship_pb2.Coordinates(coordinates=coordinates)
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = spaceship_pb2_grpc.ReportingServiceStub(channel)
        for ship in stub.ReportSpaceships(coordinates):
            try:
                spaceship = m.Spaceship(
                    alignment="Ally" if ship.alignment == spaceship_pb2.Alignment.ALLY else "Enemy",
                    name=ship.name,
                    class_=spaceship_pb2.Class.Name(ship.class_).capitalize(),
                    length=ship.length,
                    crew_size=ship.crew_size,
                    armed=ship.armed,
                    officers=[{"first_name": officer.first_name, "last_name": officer.last_name,
                               "rank": officer.rank} for officer in ship.officers]
                )
                print(json.dumps(spaceship.dict()))
                save_spaceship(db, spaceship.dict(by_alias=True))
            except ValidationError:
                print("Validation is failed")


def list_traitors(db):
    traitors_query = text("""
    SELECT first_name, last_name, rank
    FROM officers
    WHERE id IN (
        SELECT officer_id
        FROM spaceship_officers
        JOIN spaceships ON spaceship_officers.spaceship_id = spaceships.id
        WHERE spaceships.alignment = 'Enemy'
    )
    AND id IN (
        SELECT officer_id
        FROM spaceship_officers
        JOIN spaceships ON spaceship_officers.spaceship_id = spaceships.id
        WHERE spaceships.alignment = 'Ally'
    )
    """)
    traitors = db.execute(traitors_query).fetchall()
    return [dict(first_name=t.first_name, last_name=t.last_name, rank=t.rank) for t in traitors]


def run_scan(coordinates):
    db = next(get_db())
    scan_coordinates(db, coordinates)


def run_list_traitors():
    db = next(get_db())
    traitors = list_traitors(db)
    for traitor in traitors:
        print(json.dumps(traitor))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["scan", "list_traitors"])
    parser.add_argument("ah", type=int, nargs='?', default=None)
    parser.add_argument("am", type=int, nargs='?', default=None)
    parser.add_argument("as_", type=float, nargs='?', default=None)
    parser.add_argument("dd", type=int, nargs='?', default=None)
    parser.add_argument("dm", type=int, nargs='?', default=None)
    parser.add_argument("ds", type=float, nargs='?', default=None)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    if args.command == 'scan':
        if None in [args.ah, args.am, args.as_, args.dd, args.dm, args.ds]:
            print("Coordinates must contain 6 numbers!")
            exit()
        coordinates = f"{args.ah} {args.am} {args.as_} {args.dd} {args.dm} {args.ds}"
        run_scan(coordinates)
    elif args.command == 'list_traitors':
        run_list_traitors()
