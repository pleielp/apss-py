
def solution(n, m):
    cache = [[-1 for _ in range(m+1)] for _ in range(n+2)]
    
    def climb(height, day):
        if cache[height][day] != -1:
            return cache[height][day]

        if height >= n:
            return 1

        if day == m:
            return 0
        
        result = .75 * climb(height + 2, day + 1) +  .25* climb(height + 1,day +1)
        cache[height][day] = result
        return cache[height][day]
    return climb(0, 0)

import sys
sys.setrecursionlimit(10000)
def solution2(height, days):
    rains = height - days
    if rains < 0:
        return 1.
    cache = [[-1 for _ in range(days+1)] for _ in range(rains+1)]
    def climb(count, day):
        if cache[count][day] != -1:
            return cache[count][day]

        if count <= 0:
            return 1

        if day == m:
            return 0

        cache[count][day] = (0.75)*climb(count - 1, day+1)  + (0.25)*climb(count, day+1)
        return cache[count][day]
    return climb(rains, 0)

C = int(input())

for _ in range(C):
    n, m = tuple(map(int, input().split()))
    print(solution2(n, m))