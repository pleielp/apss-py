"""Return min length of palindromes made from originimal strings

url: https://algospot.com/judge/problem/read/PALINDROMIZE
ID : PALINDROMIZE
"""
def get_partial_match(strng):
    N = len(strng)
    pi = [0] * N
    begin, matched = 1, 0

    while begin + matched < N:
        if strng[begin + matched] == strng[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]
    return pi


def max_overlaped_chars(s1, s2):
    N = len(s2)
    pi = get_partial_match(s2)
    begin = matched = 0

    while begin < N:
        if matched < N and s1[begin+matched] == s2[matched]:
            matched += 1
            if begin + matched == N:
                return matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]

    return 0


def min_palindromize(strng):
    reversed_strng = strng[::-1]
    max_overlaps = max_overlaped_chars(strng, reversed_strng)

    return strng + reversed_strng[:-max_overlaps]


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        strng = input().strip()
        ans.append(len(min_palindromize(strng)))

    for n in ans:
        print(n)
