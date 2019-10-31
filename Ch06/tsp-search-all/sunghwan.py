def tsp(dist_graph):
    N = len(dist_graph)
    VISITED_ALL = (1 << N) - 1
    INF = float('inf')

    def travel(path, visited):
        if visited == VISITED_ALL:
            return 0

        last = path[-1]
        ret = INF

        for nxt in range(N):
            if visited & (1 << nxt) == 0:
                ret = min(ret, travel(path + [nxt], visited | (1 << nxt)) + dist_graph[last][nxt])
        return ret

    return min(travel([n], 1 << n) for n in range(N))


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        N = int(input())
        dist_graph = []
        for _ in range(N):
            dist_graph.append([float(n) for n in input().split()])
        ans.append(tsp(dist_graph))

    for n in ans:
        print(n)
