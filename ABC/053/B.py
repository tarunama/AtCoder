s = input()


def main(s):
    a_index = 200000 
    z_index = -1
    i = 0

    for c in s:
        if c == 'A':
            a_index = min(a_index, i)
        elif c == 'Z':
            z_index = max(z_index, i)
        i += 1

    return (z_index - a_index) + 1


print(main(s))
