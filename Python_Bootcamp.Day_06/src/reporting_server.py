import random
from concurrent import futures
import grpc
import spaceship_pb2
import spaceship_pb2_grpc


class ReportingService(spaceship_pb2_grpc.ReportingServiceServicer):
    def ReportSpaceships(self, request, context):
        for _ in range(random.randint(1, 10)):
            alignment = random.choice([spaceship_pb2.Alignment.ALLY, spaceship_pb2.Alignment.ENEMY])
            officers = []
            if alignment == spaceship_pb2.Alignment.ALLY or random.random() < 0.7:
                officers = [
                    spaceship_pb2.Officer(
                        first_name="First" + str(i),
                        last_name="Last" + str(i),
                        rank="Rank" + str(i)
                    ) for i in range(random.randint(1, 10))
                ]


            ship = spaceship_pb2.Spaceship(
                alignment=alignment,
                name=random.choice(["Normandy", "Executor"]) if random.random() < 0.8 else random.choice(
                    ["Normandy", "Executor", "Unknown"]),
                class_=random.choice([
                    spaceship_pb2.Class.CORVETTE,
                    spaceship_pb2.Class.FRIGATE,
                    spaceship_pb2.Class.CRUISER,
                    spaceship_pb2.Class.DESTROYER,
                    spaceship_pb2.Class.CARRIER,
                    spaceship_pb2.Class.DREADNOUGHT,
                ]),
                length=random.randint(80, 5000) if random.random() < 0.8 else random.randint(80, 20000),
                crew_size=random.randint(0, 250) if random.random() < 0.8 else random.randint(0, 500),
                armed=bool(random.getrandbits(1)),
                officers=officers
            )
            yield ship


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    spaceship_pb2_grpc.add_ReportingServiceServicer_to_server(ReportingService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
