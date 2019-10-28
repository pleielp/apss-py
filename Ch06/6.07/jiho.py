n = 10

weight = [[9 for _ in range(n)]for _ in range(n)]


def non_recursive_shortest_path():
    ans = float('inf')
    stack = [([0], list(range(1, n)), 0)]
    while stack:
        visited, citys, length = stack.pop()
        for idx, city in enumerate(citys):
            new_visited = visited[:] + [city]
            new_citys = citys[:idx] + citys[idx+1:]
            new_length = length + weight[visited[-1]][city]
            if len(new_citys) == 0:
                ans = min(ans, new_length + weight[0][city])
            else:
                stack.append((new_visited, new_citys, new_length))
    return ans


weight = [[0 for _ in range(n)]for _ in range(n)]
citys = list(range(n))


def shortest_path(visited, length):
    if len(visited) == n:
        return length + weight[visited[-1]][0]
    ret = float('inf')

    for city in citys:
        if city in visited:
            continue
        visited.append(city)
        ret = min(ret, shortest_path(
            visited, length + weight[city][visited[-1]]))
        visited.pop()

    return ret
