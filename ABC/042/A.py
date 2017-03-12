ss = [int(e) for e in input().split()]
 
 
def main(ss):
    five_count = ss.count(5)
    seven_count = ss.count(7)
    if five_count == 2 and seven_count == 1:
        return 'YES'
    else:
        return 'NO'
 
 
print(main(ss))