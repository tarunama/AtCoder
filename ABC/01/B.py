m = int(input())
 
 
def main(m):
    m = m / 1000
 
    if m < 0.1:
        vv = 0
    elif 0.1 <= m <= 5.0:
        vv = m * 10
    elif 6.0 <= m <= 30.0:
        vv = m + 50
    elif 35.0 <= m <= 70.0:
        vv = (m - 30) // 5 + 80
    else:
        vv = 89
 
    return int(vv)
 
ans = main(m)
 
 
print('{0:02d}'.format(ans))
