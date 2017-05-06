 # -*- coding: utf-8 -*-
 
 
a, b, c = [int(e) for e in input().split()]


if a == b == c == 1:
    print(0)
elif a == b == c: 
    print(-1)
else:
    count = 0
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        aa, bb, cc = a, b, c
        a = bb // 2 + cc // 2
        b = aa // 2 + cc // 2
        c = aa // 2 + bb // 2
        count += 1
    print(count)
