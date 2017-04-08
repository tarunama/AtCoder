# -*- coding: utf-8 -*-
 
def list_n():
    return [int(e) for e in input().split()]
 
 
 
def main(a, b, c):
    if b - a == c - b:
        return 'YES'
    else:
        return 'NO'
 
if __name__ == '__main__':
    a, b, c = list_n()
    print(main(a, b, c))
