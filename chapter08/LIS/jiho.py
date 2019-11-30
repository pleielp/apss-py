def solution(seq):
    cache = [-1 for _ in range(len(seq)+1)]

    def lis(idx):
        if cache[idx + 1] != -1:
            return cache[idx + 1]

        ret = 1
        for i in range(idx + 1, len(seq)):
            if idx == -1 or seq[i] > seq[idx]:
                ret = max(ret, lis(i) + 1)

        cache[idx + 1] = ret
        return ret

    return lis(-1) - 1


C = int(input())

for _ in range(C):
    _ = input()
    sequence = list(map(int, input().split()))
    print(solution(sequence))
