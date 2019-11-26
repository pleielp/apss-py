cache = None

def bino2(n, r, level=1):
    global cache
    
    if level == 1:
        cache = [[-1] * (r + 1) for _ in range(n)]
        
    if r == 0 or n == r:
        return 1
    
    ret = cache[n-1][r]
    
    if ret != -1:
        return ret

    cache[n-1][r] = bino2(n - 1, r - 1, level=level+1) + bino2(n - 1, r, level=level+1)

    return cache[n-1][r]


print(bino2(8, 4))