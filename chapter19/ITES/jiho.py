from collections import deque


def solution(K, N):
    ret = 0
    rangeSum = 0
    signals = deque()
    for signal in signal_generator(N):
        signals.append(signal)
        rangeSum += signal

        while rangeSum > K:
            rangeSum -= signals.popleft()

        if rangeSum == K:
            ret += 1

    return ret


def signal_generator(n):
    seed = 1983

    for _ in range(n):
        signal = seed % 10000 + 1
        yield signal

        seed *= 214013
        seed += 2531011
        seed %= 2 ** 32


C = int(input())
for _ in range(C):
    K, N = map(int, input().split())
    print(solution(K, N))
