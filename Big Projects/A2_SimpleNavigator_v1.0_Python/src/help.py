import random


class Stack:
    def __init__(self):
        self.data = []

    def empty(self):
        return self.data == []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]


class Queue:
    def __init__(self):
        self.data = []

    def empty(self):
        return self.data == []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop(0)

    def front(self):
        return self.data[0]

    def back(self):
        return self.data[-1]


class Ant:
    def __init__(self, start_position, alfa, betta):
        self.start_position = start_position
        self.path = []
        self.path_length = 0
        self.alfa = alfa
        self.betta = betta

    def make_step(self, weight_graph, pheromones, position: int):
        s = len(weight_graph)
        variants = [i for i in range(s) if weight_graph[position][i] > 0 and i not in self.path]
        if len(variants) == 0:
            variants = [self.start_position]
        wish_sum = sum([(pheromones[position][i] ** self.alfa) * (weight_graph[position][i] ** self.betta)
                        for i in variants])
        wish_list = [((pheromones[position][i] ** self.alfa) * (weight_graph[position][i] ** self.betta)) / wish_sum
                     for i in variants]
        rand_num = round(random.random(), 2)
        choice = -1
        interval = 0
        for i in range(len(wish_list) - 1):
            if interval <= rand_num < interval + wish_list[i + 1]:
                choice = variants[i]
                break
            interval += wish_list[i]
        else:
            choice = variants[len(wish_list) - 1]
        self.path.append(choice)
        self.path_length += weight_graph[position][choice]
        return choice

    def make_path(self, weight_graph, pheromones):
        position = self.start_position
        self.path.append(position)
        pos = -1
        while self.start_position != pos:
            position = self.make_step(weight_graph, pheromones, position)
            pos = position

        return self.path_length


def correct_path(path):
    pos = path.index(1)
    return path[pos:-1] + path[:pos] + [1]
