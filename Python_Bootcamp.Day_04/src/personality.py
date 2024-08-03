import random


def turrets_generator():
    values = [random.randint(0, 100) for _ in range(5)]
    lst = [i * 100 // sum(values) for i in values]
    lst[-1] += 100 - sum(lst)

    return type("Turret", (),
                {"neuroticism": lst[0],
                 "openness": lst[1],
                 "conscientiousness": lst[2],
                 "extraversion": lst[3],
                 "agreeableness": lst[4],
                 "shoot": lambda self: print("Shooting"),
                 "search": lambda self: print("Searching"),
                 "talk": lambda self: print("Talking")})()


if __name__ == "__main__":
    a = turrets_generator()
    print(a.neuroticism, a.openness, a.conscientiousness, a.extraversion, a.agreeableness)
    print(a.neuroticism + a.openness + a.conscientiousness + a.extraversion + a.agreeableness)
    a.shoot()
    a.search()
    a.talk()
