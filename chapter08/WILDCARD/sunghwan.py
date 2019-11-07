"""Return file names which match wildcard patterns

:input:
2
he?p
3
help
heap
helpp
*p*
3
help
papa
hello

:return:
heap
help
help
papa

url: https://algospot.com/judge/problem/read/WILDCARD
ID : WILDCARD
"""
# Exhaustive one
def names_that_match(pattern, names):
    ans = []

    def do_match(pat, name):
        pos = 0
        while pos < len(pat) and pos < len(name) \
            and (pat[pos] == '?' or pat[pos] == name[pos]):
            pos += 1

        if pos == len(pat):
            return pos == len(name)

        if pat[pos] == '*':
            for skip in range(len(name)-pos+1):
                if do_match(pat[pos+1:], name[pos+skip:]):
                    return True

        return False


    for name in names:
        if do_match(pat, name):
            ans.append(name)

    return ans


# Dynamic programming one
def do_name_match(pattern, name):
    P, N = len(pattern), len(name)
    cache = [[-1] * (N+1) for _ in range(P+1)]

    def match_memoized(p, n):
        if cache[p][n] != -1:
            return cache[p][n]

        while p < P and n < N \
              and (pattern[p] == '?' or pattern[p] == name[n]):
            cache[p][n] = match_memoized(p+1, n+1)
            return cache[p][n]

        if p == P:
            cache[p][n] = (n == N)
            return cache[p][n]

        if pattern[p] == '*':
            if match_memoized(p+1, n) or (n < N and match_memoized(p, n+1)):
                cache[p][n] = True
                return True

        cache[p][n] = False
        return False

    return match_memoized(0, 0)


if __name__ == '__main__':
    C = int(input())

    for _ in range(C):
        pat = input()
        N = int(input())
        ans = []

        for _ in range(N):
            name = input()
            if do_name_match(pat, name):
                ans.append(name)

        for name in sorted(ans):
            print(name)
