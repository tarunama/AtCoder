n = int(input())
 
 
def main(n):
    get = n // 15 * 200
    pay = n * 800
    return pay - get
 
 
ans = main(n)
print(ans)
