from collections import deque


def signal_generator(n):
    seed = 1983

    for _ in range(n):
        signal = seed % 10000 + 1
        yield signal

        seed *= 214013
        seed += 2531011
        seed %= 2 ** 32


def solution(k, n):
    signals = deque()
    sum_signals = 0
    answer = 0

    for signal in signal_generator(n):
        signals.append(signal)
        sum_signals += signal

        while sum_signals > k:
            sum_signals -= signals.popleft()

        if sum_signals == k:
            answer += 1

    return answer


case_num = int(input())
for _ in range(case_num):
    k, n = map(int, input().strip().split())
    print(solution(k, n))
