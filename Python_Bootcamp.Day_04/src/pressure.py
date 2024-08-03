from random import randrange, randint
from time import sleep


def emit_gel(step):
    cur_step = step
    while True:
        liquid_value = randrange(50, 100) + randint(min(0, cur_step), max(0, cur_step))
        if liquid_value < 10 or liquid_value > 90:
            return
        new_step = yield liquid_value
        if new_step is not None:
            cur_step = new_step
        else:
            cur_step = step
        sleep(0.1)


def valve():
    step = 1
    gen = emit_gel(step)
    try:
        while True:
            value = next(gen)
            if value < 20 or value > 80:
                print(gen.send(-step))
            else:
                print(value)
    except StopIteration:
        print("Generator stopped")


if __name__ == "__main__":
    valve()
