def solution(today, start, town_bridge, result_towns):

    cache = [[-1 for _ in range(len(town_bridge))] for _ in range(today+1)]
    degree = tuple(map(lambda x: sum(x), town_bridge))

    def get_prob(day, town):
        if cache[day][town] != -1:
            return cache[day][town]
        
        if day == 0:
            return 1 if town == start else 0

        ret = 0
        for near_town, bridge in enumerate(town_bridge[town]):
            if bridge:
                ret += get_prob(day - 1, near_town) / degree[near_town]
        
        cache[day][town] = ret
        return ret

    result = ""
    for idx, result_town in enumerate(result_towns):
        if idx!=0:
            result = result + " "
        result = result + str(get_prob(today, result_town))
    return result

C = int(input())
for _ in range(C):
    n, day, start = tuple(map(int, input().split()))
    
    town_bridge = []
    for _ in range(n):
        town_bridge.append(tuple(map(int, input().split())))
    _  = input()
    result_towns = tuple(map(int, input().split()))
    print(solution(day, start, town_bridge, result_towns))