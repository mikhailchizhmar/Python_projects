class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for elem in self.iterable:
            pos, neg = 0, 0
            for f in self.funcs:
                res = f(elem)
                if res:
                    pos += 1
                else:
                    neg += 1

            if self.judge(pos, neg):
                yield elem


def f2(x):
    return x % 2 == 0


def f3(x):
    return x % 3 == 0


def f5(x):
    return x % 5 == 0


a = [i for i in range(30)] + [60]
multi1 = list(multifilter(a, f2, f3, f5, judge=multifilter.judge_all))
print(a)
print(multi1)
