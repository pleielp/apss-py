def match(w, s):
    pos = 0
    while pos < len(s) and pos < len(w) and (w[pos] == '?' or w[pos] == s[pos]):
        pos += 1

    if pos == len(w):
        return pos == len(s)

    if w[pos] == "*":
        for skip in range(0, len(s)-pos+1):
            if match(w[pos+1:], s[pos+skip:]):
                return True
    return False


def dp_match(wild, string):
    # W[w:] S[s:]
    wild_length = len(wild)
    string_length = len(string)
    cache = [[-1 for _ in range(string_length+1)]
             for _ in range(wild_length+1)]

    def match(w, s):
        if cache[w][s] != -1:
            return cache[w][s]

        while w < wild_length and s < string_length and (wild[w] == "?" or wild[w] == string[s]):
            w += 1
            s += 1

        if w == wild_length:
            ret = (s == string_length)
            cache[w][s] = ret
            return ret

        if wild[w] == '*':
            for skip in range(0, string_length - s + 1):
                if match(w+1, s+skip):
                    return True

        cache[w][s] = False
        return False

    return match(0, 0)


answer = []
C = int(input())
for _ in range(C):
    expr = input()
    n = int(input())
    for _ in range(n):
        text = input()
        if dp_match(expr, text):
            answer.append(text)

for a in answer:
    print(a)
