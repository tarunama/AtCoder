# できなかった点
# 整数のみで計算できるように適切な式変形

n, x = map(int, input().split())

now = 0

for i in range(n):
    v, p = map(int, input().split())
    now += v * p
    if now > x * 100:
        print(i + 1)
        exit()
print(-1)
