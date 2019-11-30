from sys import setrecursionlimit
setrecursionlimit(10000)


def solution(pi):
    cache = [-1 for _ in range(len(pi)+1)]

    def measure_level(start, end):
        # 1 same numbers
        is_same = True
        for i in range(start, end):
            if pi[start] != pi[i]:
                is_same = False
                break
        if is_same:
            return 1

        # 2
        is_monotone = True
        gap = pi[start] - pi[start+1]
        if abs(gap) == 1:
            for i in range(start, end - 1):
                if pi[i] - pi[i+1] != gap:
                    is_monotone = False
                    break
            if is_monotone:
                return 2

        # 3
        substr = pi[start:end]
        even = substr[0]
        odd = substr[1]
        for i in range(len(substr)):
            if i % 2 == 0 and even != substr[i]:
                break
            if i % 2 == 1 and odd != substr[i]:
                break
        else:
            return 4

        # 4
        gap = pi[start] - pi[start+1]
        for i in range(start, end - 1):
            if pi[i] - pi[i+1] != gap:
                break
        else:
            return 5

        return 10

    def get_min_level(idx):
        if cache[idx] != -1:
            return cache[idx]

        if idx == len(pi):
            return 0

        ret = float('inf')
        # 3 ~ 5
        for unit in range(3, 6):
            if idx + unit > len(pi):
                continue

            ret = min(ret, get_min_level(idx + unit) +
                      measure_level(idx, idx + unit))

        cache[idx] = ret
        return ret

    return get_min_level(0)


C = int(input())

for _ in range(C):
    pi = list(map(int, input().strip()))
    print(solution(pi))
