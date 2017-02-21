n = int(input())
 
 
mod_num = pow(10, 9) + 7
 
 
def main(n):
    ret = 1
    for i in range(1, n + 1):
        ret = ret * i % mod_num
    return ret
    
 
answer = main(n)
print(answer)
