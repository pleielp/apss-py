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


def longest_frequent(k, s):
    suffix_array = get_suffix_array(s)
    ret = 0
    for i in range(len(s) - k + 1):
        ret = max(ret, common_prefix(s, suffix_array[i], suffix_array[i+k-1]))
    return ret
    

if __name__ == "__main__":
    case_num = int(input())
    for _ in range(case_num):
        k = int(input())
        script = input().strip()
        print(longest_frequent(k, script))
