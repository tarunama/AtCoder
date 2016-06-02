# -*- coding: utf-8 -*-


def solve(test_data=None):
    l = [0, 0]
    s = input()
    t = int(input())
    d = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }

    ret = []
    for c in s:
        direct = d.get(c)
        if direct:
            l[0] += direct[0]
            l[1] += direct[1]
        else:
            if t == 1:
                if 0 <= l[0] and 0 <= l[1]:
                    if abs(l[0]) < abs(l[1]):
                        l[0] += 1
                    else:
                        l[1] += 1
                elif 0 <= l[0] and l[1] < 0:
                    if abs(l[0]) < abs(l[1]):
                        l[0] += 1
                    else:
                        l[1] -= 1
                elif l[0] < 0 and 0 <= l[1]:
                    if abs(l[0]) < abs(l[1]):
                        l[0] -= 1
                    else:
                        l[1] += 1
                else:
                    if abs(l[0]) < abs(l[1]):
                        l[0] -= 1
                    else:
                        l[1] -= 1
            elif t == 2:
                if 0 <= l[0] and 0 <= l[1]:
                    if abs(l[0]) < abs(l[1]):
                        l[0] += 1
                    else:
                        l[1] += 1
                elif 0 <= l[0] and l[1] < 0:
                    if abs(l[0]) < abs(l[1]):
                        l[0] -= 1
                    else:
                        l[1] += 1
                elif l[0] < 0 and 0 <= l[1]:
                    if abs(l[0]) < abs(l[1]):
                        l[0] += 1
                    else:
                        l[1] -= 1
                else:
                    if abs(l[0]) < abs(l[1]):
                        l[0] += 1
                    else:
                        l[1] += 1
        ret.append(l)

    _sum = map(lambda lst: abs(lst[0]) + abs(lst[1]), ret)
    if t == 1:
        print(max(_sum))
    else:
        print(min(_sum))


if __name__ == '__main__':
    solve()