# -*- coding: utf-8 -*-


n, m = [int(e) for e in input().split()]
qs = []
for f, t in input().split():
    qs.append([f, t])


def main(n, m, qs):
    l = [[e, 0] for e in range(1, n + 1) if e != 1]
    
    for _from , to in range(qs):
        pass
