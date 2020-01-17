def get_suffix_array(s):
    n = len(s)
    s += ' ' * n
    t = 1
    group = list(s) + ['']
    perm = [i for i in range(n)]

    while t < n:
        perm.sort(key=(lambda x: (group[x], s[x+t-1])))
        # print(perm)

        new_group = [0] * n + [-1]
        new_group[perm[0]] = 0
        for j in range(1, n):
            if s[perm[j]:perm[j]+t] == s[perm[j-1]:perm[j-1]+t]:
                new_group[perm[j]] =  new_group[perm[j-1]]
            else:
                new_group[perm[j]] =  new_group[perm[j-1]] + 1
        group = new_group
        t *= 2
        # print(group)

    return perm


if __name__ == "__main__":
    print(get_suffix_array('banana'))
    print(get_suffix_array('alohomora'))