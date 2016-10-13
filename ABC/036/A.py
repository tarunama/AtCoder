# -*- coding: utf-8 -*-


a, b = map(int, input().split())


def main(a, b):
    i = 1
    while a * i < b:
        i += 1
    return i


print(main(a, b))
