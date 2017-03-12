n = int(input())
ans = 10 ** 9


for w in range(1, n + 1):
    h = int(n // w)
    area = h * w
    abs_diff = abs(h - w)

    if (n - area) + abs_diff < ans:
        ans = (n - area) + abs_diff


print(ans)
