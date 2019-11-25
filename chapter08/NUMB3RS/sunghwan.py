"""Get probabilities of Doctor Dunibals staying in villages

url: https://algospot.com/judge/problem/read/NUMB3RS
ID : NUMB3RS
"""
def get_probability(graph, targets, DAYS, PRISON):
    N = len(graph)
    NOT_CONNECTED, CONNECTED = range(2)
    degree_cache = [0] * N
    cache = [[-1] * (DAYS + 1) for _ in range(N)]

    for v in range(N):
        degree_cache[v] = sum(e == CONNECTED for e in graph[v])

    def probability_in_here(v, d):
        if d == 0:
            return 1 if v == PRISON else 0
        if cache[v][d] != -1:
            return cache[v][d]

        ret = 0
        for n in range(N):
            if graph[n][v] == CONNECTED:
                ret += probability_in_here(n, d-1) / degree_cache[n]

        cache[v][d] = ret
        return ret

    return [probability_in_here(t, DAYS) for t in targets]


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N, D, P = (int(n) for n in input().split())
        graph = []
        for _ in range(N):
            graph.append([int(n) for n in input().split()])

        input()
        targets = tuple(int(n) for n in input().split())

        probs = get_probability(graph, targets, D, P)
        ans.append(' '.join(str(n) for n in probs))

    for p in ans:
        print(p)
