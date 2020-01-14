def get_partial_match(s: str):
    pi = [0] * len(s)
​
    begin = 1
    matched = 0
    while begin + matched < len(s):
        if s[begin + matched] == s[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi
​
​
def solution(a, b):
    m = len(a)
    n = len(b)
    pi = get_partial_match(b)
    begin = 0
    matched = 0
    while begin < m:
        if matched < n and a[begin + matched] == b[matched]:
            matched += 1
            if begin + matched == m:
                return matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return 0
​
​
C = int(input())
​
for _ in range(C):
​
    text = input()
    reverse_text = text[::-1]
    overlap = solution(text, reverse_text)
    print(2 * len(text) - overlap)