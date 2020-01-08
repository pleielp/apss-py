"""Return how many ticks are needed here

url: https://algospot.com/judge/problem/read/JAEHASAFE
ID : JAEHASAFE
"""
import sys

input = sys.stdin.readline


def kmp(haystack, needle):
    H, N = len(haystack), len(needle)
    pi = get_partial_match(needle)
    begin = matched = 0

    while begin <= H - N:
        if matched < N and haystack[begin + matched] == needle[matched]:
            matched += 1
            if matched == N:
                return begin
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]

    return -1


def get_partial_match(needle):
    N = len(needle)
    pi = [0] * N
    begin, matched = 1, 0

    while begin + matched < N:
        if needle[begin + matched] == needle[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


def min_ticks_needed(states, anticlockwise=False):
    ans = 0

    for i in range(len(states)-1):
        now, target = states[i:i+2]
        if anticlockwise:
            ans += kmp(now * 2, target)
        else:
            ans += kmp(target * 2, now)

        anticlockwise ^= True

    return ans


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N = int(input()) + 1
        states = []
        for _ in range(N):
            states.append(input().strip())

        ans.append(min_ticks_needed(states))

    for n in ans:
        print(n)
