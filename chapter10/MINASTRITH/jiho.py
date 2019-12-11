import math
def solution(defenses):
    defense_thetas = []
    for y, x, r in defenses:
        middle_theta = math.fmod(2*math.pi + math.atan2(y, x), 2*math.pi)
        theta = 2 * math.asin(r/(2*8))
        begin = middle_theta - theta
        end = middle_theta + theta
        defense_thetas.append((begin, end))
    defense_thetas.sort()
    
    def solveCircular():
        ret = float('inf')
        for first, second in defense_thetas:
            if first <= 0 or second >= 2*math.pi:
                begin = math.fmod(second, 2*math.pi)
                end = math.fmod(first + 2*math.pi, 2*math.pi)
                ret = min(ret, 1 + solveLinear(begin, end))
        return ret
    
    def solveLinear(begin, end):
        used = 0
        idx = 0
        while begin < end:
            maxCover = -1
            while idx < len(defense_thetas) and defense_thetas[idx][0] <= begin:
                maxCover = max(maxCover, defense_thetas[idx][1])
                idx += 1
            if maxCover <= begin:
                return float('inf')
            begin = maxCover
            used += 1
        return used

    return solveCircular()
    
C = int(input())

for _ in range(C):
    point_num = int(input())
    circles = []
    for _ in range(point_num):
        circles.append(tuple(map(float,input().split())))
    result = solution(circles)
    print("IMPOSSIBLE" if float('inf') == result else result )