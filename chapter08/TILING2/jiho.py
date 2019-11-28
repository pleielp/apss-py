def solution(width):
    cache = [-1 for _ in range(width + 1)]

    def tiling(n):
        
        if cache[n] != -1:
            return cache[n]
        
        if n == 0 or n == 1:
            return 1

        cache[n] = tiling(n-1) + tiling(n - 2)
        
        return cache[n] % 1000000007

    return tiling(width)

C = int(input())
for _ in range(C):
    print(solution(int(input())))