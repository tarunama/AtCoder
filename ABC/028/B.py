# -*- coding: utf-8 -*-
from collections import OrderedDict


d = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
}

def solve(test_data=None):
    s = input()

    for ch in s:
        d[ch] += 1

    _d = OrderedDict(sorted(d.items(), key=lambda e: e[0]))

    print(" ".join([str(e) for e in _d.values()]))


if __name__ == "__main__":
    solve()
