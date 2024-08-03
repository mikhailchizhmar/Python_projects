from ex00 import add_ingot
from typing import Dict


def split_booty(*args: [Dict[str, int]]):
    count_gold = 0
    for purse in args:
        if "gold_ingots" in purse:
            count_gold += purse["gold_ingots"]
    purse1 = {}
    purse2 = {}
    purse3 = {}
    for _ in range(count_gold // 3):
        purse1 = add_ingot(purse1)
    count_gold -= count_gold // 3
    for _ in range(count_gold // 2):
        purse2 = add_ingot(purse2)
    count_gold -= count_gold // 2
    for _ in range(count_gold):
        purse3 = add_ingot(purse3)
    return purse1, purse2, purse3


if __name__ == '__main__':
    print(split_booty({"gold_ingots": 6}, {"gold_ingots": 6}))
    print(split_booty({"gold_ingots": 1}, {"gold_ingots": 1}, {"gold_ingots": 9}))
    print(split_booty({"gold_ingots": 10}, {"apples": 10}))
