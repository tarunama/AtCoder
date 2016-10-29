s = input()


def main(s):
    if 'C' in s and 'F' in s:
        for i in range(s.count('C')):
            if i != 0:
                s_l = list(s)
                del s_l[c_i]
                s = ''.join(s_l)
            c_i = s.index('C')
        for i in range(s.count('F')):
            if i != 0:
                s_l = list(s)
                del s_l[f_i]
                s = ''.join(s_l)
            f_i = s.index('F')

        if c_i <= f_i:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'

print(main(s))
