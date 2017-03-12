n, str_len = [int(e) for e in input().split()]
strs = [input() for _ in range(n)]
 
 
def main(n, str_len, strs):
    ordered_strs = sorted(strs)
    return ''.join(ordered_strs)
 
 
print(main(n, str_len, strs))