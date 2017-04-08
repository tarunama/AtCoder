# -*- coding: utf-8 -*-
from collections import deque
 
 
def list_n():
    return [int(e) for e in input().split()]
 
 
def main(o, e):
    answer = ''
    o = deque(o)
    e = deque(e)
    for i in range(len(o) + len(e)):
        if i % 2 == 0:
            answer += o.popleft()
        else:
            answer += e.popleft()
    return answer


if __name__ == '__main__':
    o = input()
    e = input()
    print(main(o, e))
