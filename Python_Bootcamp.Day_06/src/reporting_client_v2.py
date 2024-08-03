import argparse
import grpc
import json
import spaceship_pb2
import spaceship_pb2_grpc
from pydantic import ValidationError
import models as m


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("ah", type=int)
    parser.add_argument("am", type=int)
    parser.add_argument("as_", type=float)
    parser.add_argument("dd", type=int)
    parser.add_argument("dm", type=int)
    parser.add_argument("ds", type=float)
    return parser.parse_args()


def run():
    try:
        args = parse_args()
        args = f'{args.ah} {args.am} {args.as_} {args.dd} {args.dm} {args.ds}'
    except:
        print("Coordinates must contain 6 numbers!")
        exit()

    coordinates = spaceship_pb2.Coordinates(coordinates=args)
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
            except ValidationError:
                print("Validation is failed")


if __name__ == '__main__':
    run()

# valid example:

# spaceship = m.Spaceship(
#     alignment="Ally",
#     name="Normandy",
#     class_='Corvette',
#     length=100,
#     crew_size=6,
#     armed=True,
#     officers=[{"first_name": officer.first_name, "last_name": officer.last_name,
#                "rank": officer.rank} for officer in ship.officers]
# )
