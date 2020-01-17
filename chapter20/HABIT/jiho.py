from functools import cmp_to_key


def generate_comparator(group: list, t: int):
    def compare(a: int, b: int):
        if group[a] != group[b]:
            if group[a] < group[b]:
                return -1
            else:
                return 0
        else:
            if group[a+t] < group[b+t]:
                return -1
            else:
                return 0
    return compare


def get_suffix_array(s: str):
    n = len(s)
    group = [ord(c) for c in s]
    group.append(-1)
    t = 1
    perm = list(range(n))

    while t < n:
        compare = generate_comparator(group, t)
        perm = sorted(perm, key=cmp_to_key(compare))
        t *= 2
        if t >= n:
            break

        new_group = [0] * n
        new_group.append(-1)
        new_group[perm[0]] = 0
        for i in range(1, n):
            if compare(perm[i-1], perm[i]):
                new_group[perm[i]] = new_group[perm[i-1]] + 1
            else:
                new_group[perm[i]] = new_group[perm[i-1]]
        group = new_group
    return perm


def get_common_prefix(s: str, i: int, j: int):
    k = 0
    while i < len(s) and j < len(s) and s[i] == s[j]:
        i += 1
        j += 1
        k += 1
    return k


def solution(k: int, text: str):
    a = get_suffix_array(text)
    ret = 0
    for i in range(len(a) - k):
        ret = max(ret, get_common_prefix(text, a[i], a[i + k - 1]))
    return ret


C = int(input())

for _ in range(C):
    k = int(input())
    text = input()
    print(solution(k, text))
