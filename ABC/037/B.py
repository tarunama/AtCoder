# -*- coding: utf-8 -*-


def solve(N, Q):
    d = {i + 1: 0 for i in range(N)}

    for _ in range(Q):
        start, stop, v = map(int, input().split())
        for i in range(start, stop + 1):
            d[i] = v

    for v in d.values():
        print(v)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    solve(N, Q)
