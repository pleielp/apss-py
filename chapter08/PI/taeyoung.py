import sys
sys.setrecursionlimit(10000)

def classify(start, end):
    subtext = text[start:end]
    if not (3 <= len(subtext) < 6):
        return float('inf')

    if subtext == [subtext[0]] * len(subtext):
        return 1

    progressive = True
    for i in range(len(subtext) - 1):
        if subtext[i + 1] - subtext[i] != subtext[1] - subtext[0]:
            progressive = False

    if progressive and abs(subtext[1] - subtext[0]) == 1:
        return 2

    alternating = True
    for j in range(len(subtext) - 2):
        if subtext[j + 2] != subtext[j]:
            alternating = False

    if alternating:
        return 4

    if progressive:
        return 5

    return 10


def substring(start):
    if start >= len(text):
        return 0
    if cache[start] == float('inf'):
        for L in range(3, 6):
            cache[start] = min(cache[start], classify(start, start + L) + substring(start + L))
    return cache[start]


case_num = int(input())
for _ in range(case_num):
    text = [int(char) for char in input().strip()]
    cache = [float('inf')] * 10002

    print(substring(0))