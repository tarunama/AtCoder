# -*- coding: utf-8 -*-
from math import floor


a, b, c = map(int, input().split())


def main(a, b, c):
    n = 0
    low, high = (a, b) if a < b else (b, a)

    n += floor(c / low)
    c -= n * low

    n += floor(c / high)

    return n


print(main(a, b, c))