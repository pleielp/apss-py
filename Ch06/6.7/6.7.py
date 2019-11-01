n = 3
dist = [[0, 1, 3], [2, 0, 1], [3, 2, 0]]

def shortest_path(path: list, visited: list, current_length: float):
    if len(path) == n:
        return current_length + dist[path[0]][path[-1]]

    ret = float('inf')
    for next in range(n):
        if visited[next]:
            continue
        here = path[-1]
        path.append(next)
        visited[next] = True
        cand = shortest_path(path, visited, current_length + dist[here][next])
        ret = min(ret, cand)
        visited[next] = False
        path.pop()

    return ret

print(shortest_path([0], [False] * n, 0))