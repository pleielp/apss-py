def solution(width):
    MOD = 1000000007
    cache = [-1 for _ in range(width + 1)]

    def tiling(n):
        
        if cache[n] != -1:
            return cache[n]
        
        if n == 0 or n == 1:
            return 1

        cache[n] = (tiling(n-1) + tiling(n - 2)) 
        
        return cache[n]

    all_case = tiling(width) 
    if width % 2 == 0:
        all_case -= tiling(width // 2)
        all_case -= tiling(width // 2 - 1)
    else:
        all_case -= tiling(width // 2)

    return all_case % MOD
    


C = int(input())

for _ in range(C):
    n = int(input())
    print(solution(n))