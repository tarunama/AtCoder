# -*- coding: utf-8 -*-
 
 
def main():
    k, s = map(int, input().split())
    answer = solve(k, s)
    return answer
 
 
def solve(k, s):
    count = 0
    for i in range(k + 1):
        for j in range(k + 1):
            z = s - i - j
            if 0 <= z and z <= k:
                count += 1
    return count
 
print(main())
