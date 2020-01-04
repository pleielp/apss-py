"""Return the count of consecutive subarray which sump up to K

url: https://algospot.com/judge/problem/read/ITES
ID : ITES
"""
from collections import deque

SEED = 1983


def signal_generator(seed=SEED):
    while True:
        yield seed % 10000 + 1
        seed = (seed * 214013 + 2531011) % (2 ** 32)


def count_subarray(N, K):
    tmp_arr = deque([])
    tmp_sum = 0
    count = 0
    generator = signal_generator()

    for _ in range(N):
        num = next(generator)
        tmp_arr.append(num)
        tmp_sum += num

        while tmp_sum >= K:
            if tmp_sum == K:
                count += 1
                break
            tmp_sum -= tmp_arr.popleft()

    return count


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        K, N = (int(n) for n in input().split())
        ans.append(count_subarray(N, K))

    for count in ans:
        print(count)
