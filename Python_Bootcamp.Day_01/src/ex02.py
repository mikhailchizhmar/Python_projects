from ex00 import add_ingot, get_ingot, empty
from typing import Dict


def squeak_decorator(func):
    def wrapper(purse: Dict[str, int]):
        print("SQUEAK")
        return func(purse)
    return wrapper


if __name__ == '__main__':
    purse1 = {}
    add_ingot = squeak_decorator(add_ingot)
    get_ingot = squeak_decorator(get_ingot)
    empty = squeak_decorator(empty)
    print(add_ingot(get_ingot(add_ingot(empty(purse1)))))
