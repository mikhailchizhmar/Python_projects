import json
import argparse
import redis


def process_message(msg, enemies):
    msg = json.loads(msg)
    from_account = msg["metadata"]["from"]
    to_account = msg["metadata"]["to"]
    amount = msg["amount"]

    if to_account in enemies and amount >= 0:
        msg["metadata"]["from"], msg["metadata"]["to"] = to_account, from_account

    print(json.dumps(msg))


def listen_and_print():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', type=str, required=True,
                        help="Comma-separated list of bad guy account numbers")
    args = parser.parse_args()
    bad_guys = set(map(int, args.e.split(',')))

    r = redis.Redis()
    pubsub = r.pubsub()
    pubsub.subscribe('transactions')

    print("Listening for messages...")
    for message in pubsub.listen():
        if message["type"] == "message":
            process_message(message["data"], bad_guys)


if __name__ == "__main__":
    listen_and_print()
