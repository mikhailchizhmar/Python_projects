class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError


def sum1(a, b):
    return a + b


if __name__ == "__main__":
    print(__name__)
    print('it is not an import')
