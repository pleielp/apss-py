"""Get max area of sub-rectangles in a histogram

url: https://algospot.com/judge/problem/read/FENCE
ID : FENCE
"""
def max_area(heights):
    def max_area_between(lo, hi):
        if lo == hi:
            return heights[lo]
        elif lo + 1 == hi:
            lower = min(lo, hi)
            return max(heights[lo], heights[hi], 2 * heights[lower])

        mid = (lo + hi) // 2
        left_area = max_area_between(lo, mid)
        right_area = max_area_between(mid+1, hi)

        l, r = mid, mid + 1
        height = min(heights[l], heights[r])
        area_between = 2 * height

        while lo < l or r < hi:
            if r < hi and (lo == l or heights[l-1] < heights[r+1]):
                r += 1
                height = min(height, heights[r])
            else:
                l -= 1
                height = min(height, heights[l])

            area_between = max(area_between, (r - l + 1) * height)

        return max(area_between, left_area, right_area)

    return max_area_between(0, len(heights)-1)


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        input()
        ans.append(max_area([int(n) for n in input().split()]))

    for n in ans:
        print(n)
