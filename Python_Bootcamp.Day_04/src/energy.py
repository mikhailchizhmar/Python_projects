from typing import Iterable, Any


def str_only(x: Any) -> bool:
    return isinstance(x, str)


def fix_wiring(c: Iterable, s: Iterable, p: Iterable) -> Iterable:
    c = list(filter(str_only, c))
    s = list(filter(str_only, s))
    p = list(filter(str_only, p))
    lst = list(zip(c, s, p))
    it = []

    for i, j, k in lst:
        it.append(f"plug {i} into {j} using {k}")
        c.pop(0)
        s.pop(0)
        p.pop(0)
    for j, k in zip(c, s):
        it.append(f"weld {j} to {k} without plug")
    return it


if __name__ == '__main__':
    print("TEST 1")
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']
    for cab in fix_wiring(cables, sockets, plugs):
        print(cab)
    print("_" * 15, "\n", sep="\n")

    print("TEST 2")
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]
    for cab in fix_wiring(cables, sockets, plugs):
        print(cab)
    print("_" * 15, "\n", sep="\n")
