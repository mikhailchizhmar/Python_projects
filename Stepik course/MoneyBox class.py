class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def can_add(self, v):
        if self.amount + v <= self.capacity:
            return True
        return False

    def add(self, v):
        if self.can_add(v):
            self.amount += v


x = MoneyBox(10)
x.add(5)
x.add(5)
x.add(5)
print(x.amount)
