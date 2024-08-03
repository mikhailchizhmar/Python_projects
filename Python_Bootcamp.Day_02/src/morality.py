from collections import Counter


class Player:
    def __init__(self):
        self.name = "Player"
        self.history = []

    def __str__(self):
        return self.name

    def reset_vars(self):
        self.history.clear()


class Cheater(Player):
    def __init__(self):
        super().__init__()
        self.name = "cheater"

    def decide(self, opponent):
        self.history.append("cheat")
        return "cheat"


class Cooperator(Player):
    def __init__(self):
        super().__init__()
        self.name = "cooperator"

    def decide(self, opponent):
        self.history.append("cooperate")
        return "cooperate"


class Copycat(Player):
    def __init__(self):
        super().__init__()
        self.name = "copycat"
        self.coop_count = 1

    def decide(self, opponent):
        if self.coop_count > 0:
            self.coop_count -= 1
            self.history.append("cooperate")
            return "cooperate"
        self.history.append(opponent.history[-1])
        return opponent.history[-1]

    def reset_vars(self):
        super().reset_vars()
        self.coop_count = 1


class Grudger(Player):
    def __init__(self):
        super().__init__()
        self.name = "grudger"
        self.switch_to_cheater = False

    def decide(self, opponent):
        if self.switch_to_cheater is True:
            self.history.append("cheat")
            return "cheat"
        if opponent.history and opponent.history[-1] == "cheat":
            self.switch_to_cheater = True
            self.history.append("cheat")
            return "cheat"
        self.history.append("cooperate")
        return "cooperate"

    def reset_vars(self):
        super().reset_vars()
        self.switch_to_cheater = False


class Detective(Player):
    def __init__(self):
        super().__init__()
        self.name = "detective"
        self.steps = ["cooperate", "cheat", "cooperate", "cooperate"]
        self.switch_to_copycat = False
        self.switch_to_cheater = False
        self.copycat = Copycat()

    def decide(self, opponent):
        if self.switch_to_copycat:
            result = self.copycat.decide(opponent)
        elif self.switch_to_cheater:
            result = "cheat"
        elif self.steps:
            result = self.steps.pop(0)
        elif "cheat" in opponent.history:
            self.switch_to_copycat = True
            result = self.copycat.decide(opponent)
        else:
            self.switch_to_cheater = True
            result = "cheat"
        self.history.append(result)
        return result

    def reset_vars(self):
        super().reset_vars()
        self.steps = ["cooperate", "cheat", "cooperate", "cooperate"]
        self.switch_to_copycat = False
        self.switch_to_cheater = False
        self.copycat = Copycat()


class Game:
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def get_result(self, decision1, decision2):
        if decision1 == "cooperate":
            if decision2 == "cooperate":
                return 2, 2
            return -1, 3
        else:
            if decision2 == "cooperate":
                return 3, -1
            return 0, 0

    def play(self, player1, player2):
        for _ in range(self.matches):
            res1 = player1.decide(player2)
            res2 = player2.decide(player1)
            self.registry[str(player1)] += self.get_result(res1, res2)[0]
            self.registry[str(player2)] += self.get_result(res1, res2)[1]
        player1.reset_vars()
        player2.reset_vars()

    def top3(self):
        for p in self.registry.most_common(3):
            print(p[0], p[1])


if __name__ == "__main__":
    game = Game()
    cheater = Cheater()
    cooperator = Cooperator()
    copycat = Copycat()
    grudger = Grudger()
    detective = Detective()
    players = [cheater, cooperator, copycat, grudger, detective]

    for p1 in players:
        for p2 in players:
            if str(p1) != str(p2):
                game.play(p1, p2)
    game.top3()
