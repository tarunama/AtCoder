n, x = map(int, input().split())

res = 0
a = 0

for i in range(n):
    v, p = map(int, input().split())

    al = v * p // 100
    a = a + al
    if (x < a):
        res = i + 1
        break

if res == 0:
    print(-1)
else:
    print(res)
