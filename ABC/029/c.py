# -*- coding: utf-8 -*-
# 解説見た
N = int(input())


def solve(rest, s):

    if rest == 0:
        print(s)
    else:
        for c in 'abc':
            solve(rest - 1, s + c)


if __name__ == '__main__':
    solve(N, '')
