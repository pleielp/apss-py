from functools import cmp_to_key


def generate_comparator(group: list, t: int):
    def compare(a: int, b: int):
        if group[a] != group[b]:
            if group[a] < group[b]:
                return -1
            else:
                return 0
        else:
            if group[a + t] < group[b + t]:
                return -1
            else:
                return 0

    return compare


def get_suffix_array(s: str):
    n = len(s)
    group = [ord(s[i]) for i in range(n)]
    group.append(-1)
    perm = list(range(n))
    t = 1
    while t < n:
        compare = generate_comparator(group, t)
        perm = sorted(perm, key=cmp_to_key(compare))

        t = t * 2
        if t >= n:
            break

        new_group = [0] * n
        new_group.append(-1)
        new_group[perm[0]] = 0

        for i in range(1, n):
            if compare(perm[i - 1], perm[i]):
                new_group[perm[i]] = new_group[perm[i - 1]] + 1
            else:
                new_group[perm[i]] = new_group[perm[i - 1]]
        group = new_group

    return perm


def min_shift(s: str):
    s2 = s + s
    a = get_suffix_array(s2)

    for i in range(len(a)):
        print(a[i])
        if a[i] <= len(s):
            return s2[a[i]:a[i] + len(s)]


print(min_shift("aavadakedavr"))
