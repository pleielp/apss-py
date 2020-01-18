def get_suffix_array(s):
    n = len(s)
    s += ' ' * n
    t = 1
    group = list(s) + ['']
    perm = [i for i in range(n)]

    while t < n:
        perm.sort(key=(lambda x: (group[x], s[x+t-1])))

        new_group = [0] * n + [-1]
        new_group[perm[0]] = 0
        for j in range(1, n):
            if s[perm[j]:perm[j]+t] == s[perm[j-1]:perm[j-1]+t]:
                new_group[perm[j]] =  new_group[perm[j-1]]
            else:
                new_group[perm[j]] =  new_group[perm[j-1]] + 1
        group = new_group
        t *= 2

    return perm


def common_prefix(s, i, j):
    k = 0
    while i < len(s) and j < len(s) and s[i] == s[j]:
        i += 1
        j += 1
        k += 1
    return k


def count_substrings(s):
    suffix_array = get_suffix_array(s)
    ret = 0

    for idx in range(len(s)):
        cp = 0
        if idx > 0:
            cp = common_prefix(s, suffix_array[idx-1], suffix_array[idx])
        ret += len(s) - suffix_array[idx] - cp

    return ret


if __name__ == "__main__":
    print(count_substrings('banana'))