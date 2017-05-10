def check(ns):
    len_ns = len(ns)
    for i, n in enumerate(ns):
        if i == len_ns - 1:
            continue

        if not (n > 0 and ns[i + 1] < 0):
            return True
    return False


def main(n, ns):
    count = 0
    idx   = 1
    while sum(ns) == 0 or check(ns):
        n = ns[idx]
        while not (ns[idx - 1] < 0 and n > 0):
            if 0 < ns[idx - 1]:
                n -= 1
                count += 1
            else:
                n +- 1
                count += 1
    return count


if __name__ == '__main__':
    # n = int(input())
    n = 4
    # ns = [int(e) for e in input().split()]
    ns = [1, -3, 1, 0]
    print(main(n, ns))
