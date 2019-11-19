def solve(left, right):
    if left == right:
        return heights[left]
    
    mid = (left + right) // 2

    ret = max(solve(left, mid), solve(mid + 1, right))

    lo, hi = mid, mid + 1
    height = min(heights[lo], heights[hi])

    while left < lo or hi < right:
        if hi < right and (lo == left or heights[lo-1] < heights[hi+1]):
            hi += 1
            height = min(height, heights[hi])
        else:
            lo -= 1
            height = min(height, heights[lo])
        
        ret = max(ret, height * (hi - lo + 1))

    return ret

case_num = int(input())
for _ in range(case_num):
    fence_num = int(input())
    heights = list(map(int, input().strip().split()))

    print(solve(0, len(heights) - 1))