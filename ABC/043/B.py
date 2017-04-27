# -*- coding: utf-8 -*-

def list_n():
    return [int(e) for e in input().split()]


def list_s():
    return [s for e in input().split()]


def main(s):
    ret = []
    for c in s:
        if c in ['0', '1']:
            ret.append(c)
        else:
            if ret:
                ret.pop()
    return ''.join(ret)


if __name__ == '__main__':
    s = input()
    print(main(s))
