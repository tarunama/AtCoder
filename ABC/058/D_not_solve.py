# -*- coding: utf-8 -*-
 
 
def list_n():
    return [int(e) for e in input().split()]
 
 
def list_s():
    return [s for e in input().split()]
 
 
 
def main(xs, ys):
    answer = 0
    max_x  = max(xs)
    max_y  = max(ys)
    min_x  = min(xs)
    min_y  = min(ys)
    
    def one_fold(xs, x=False):
        if len(xs) == 2:
            if x:
                return [max_x - min_x]
            else:
                return [max_y - min_y]
        else:
            return [xs[i] - xs[i - 1] for i in range(1, len(xs))]
    
    xxs = one_fold(xs)
    yys = one_fold(ys)
 
    while True:
        if len(xxs) == 1 and len(yys) == 1:
            break
 
        for x in xxs:
            for y in yys:
                answer += x * y
 
        if len(xxs) > len(yys):
            xxs = one_fold(xxs, x=True)
        else:
            yys = one_fold(yys)
    answer += max_x * max_y
    return answer % (pow(10, 9) + 7)


if __name__ == '__main__':
    n, m = list_n()
    xs   = list_n()
    ys   = list_n()
    print(main(xs, ys))
