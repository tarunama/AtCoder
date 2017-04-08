# -*- coding: utf-8 -*-


def main(n, ns):
    if len(set(ns)) == 1:
        return 0
    
    min_v  = min(ns)
    max_v  = max(ns)
    # 想定しうるコストの最大量
    answer = pow(100, 3)
    for i in range(min_v, max_v + 1):
        cost = 0
        for j in ns:
            if i == j:
                continue
            cost += pow((j - i), 2)
        answer = min(answer, cost)
    return answer
 
 
if __name__ == '__main__':
    n = int(input())
    ns = [int(e) for e in input().split()]
    print(main(n, ns))
