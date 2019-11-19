def pairing(n, pairs):
    ret = 0
    is_paired = [[0 for _ in range(n)] for _ in range(n)]
    for a, b in pairs:
        is_paired[a][b] = 1
        is_paired[b][a] = 1
    stack = [list(range(n))]
    while stack:
        remains = stack.pop()
        if len(remains) == 0:
            ret += 1
            continue
        target = remains.pop()
        for idx, remain in enumerate(remains):
            if is_paired[remain][target]:
                new_remains = remains[:idx] + remains[idx+1:]
                stack.append(new_remains)
    return ret


C = int(input())

for _ in range(C):
    n, pairs_n = tuple(map(int, input().split()))
    pairs = list(map(int, input().split()))
    pairs = [(pairs[2*p], pairs[2*p+1]) for p in range(pairs_n)]
    print(pairing(n, pairs))
