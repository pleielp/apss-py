N = input()
M = input()
​
name = N + M
​
​
pi = [0] * len(name)
matched = 0
begin = 1
answer = [len(name)]
while begin + matched < len(name):
    if name[begin + matched] == name[matched]:
        pi[begin + matched] = matched + 1
        matched += 1
    else:
        if matched == 0:
            begin += 1
        else:
            begin += matched - pi[matched - 1]
            matched = pi[matched - 1]
ret = []
k = len(name)
while k > 0:
    ret.append(k)
    k = pi[k - 1]
​
print(*ret[::-1])