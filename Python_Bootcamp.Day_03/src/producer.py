import json
import logging
import random
import redis


def generate():
    message = {
        "metadata": {
            "from": random.randint(1000000000, 9999999999),
            "to": random.randint(1000000000, 9999999999)
        },
        "amount": random.randint(-10000, 10000)
    }
    return message


def publish_messages(n=7):
    test = [{"metadata": {"from": 1111111111, "to": 2222222222}, "amount": 10000},
            {"metadata": {"from": 3333333333, "to": 4444444444}, "amount": -3000},
            {"metadata": {"from": 2222222222, "to": 5555555555}, "amount": 5000}]
    try:
        r = redis.Redis()
        for i in range(3):
            r.publish('transactions', json.dumps(test[i]))
            logging.info(f"Published message: {test[i]}")
        for _ in range(n):
            message = generate()
            r.publish('transactions', json.dumps(message))
            logging.info(f"Published message: {message}")
    except redis.exceptions.ConnectionError:
        logging.exception("[redis.exceptions.ConnectionError]", exc_info=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    publish_messages()
