from collections import deque


def solution(N, K):
    survivors = deque(range(1, N + 1))
    while len(survivors) > 2:
        survivors.popleft()
        for _ in range((K - 1) % len(survivors)):
            temp = survivors.popleft()
            survivors.append(temp)
    return sorted(list(survivors))


C = int(input())
for _ in range(C):
    N, K = map(int, input().split())
    print(" ".join(map(str, solution(N, K))))
