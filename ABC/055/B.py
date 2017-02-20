n = int(input())


mod_num = pow(10, 9) + 7


def main(n):
    pre = 1
    for i in range(2, n + 1):
        pre = pre * i % mod_num
    return pre


ans = main(n)
print(ans)
