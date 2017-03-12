candies = [int(e) for e in input().split()]
lst = sorted(candies)


def main(lst):
    max = lst[2]

    if max == lst[0] + lst[1]:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    ans = main(lst)
    print(ans)
