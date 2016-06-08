# -*- coding: utf-8 -*-


def solve(test_data=None):
    n, m = map(int, input().split())

    if n % 16 == 0 and m % 9 == 0:
        print('4:3')
    else:
        print('16:9')
    return

if __name__ == '__main__':
    solve()