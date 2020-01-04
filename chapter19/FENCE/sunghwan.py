"""Get the maximum area of the bars standing side by side

ID : FENCE
https://algospot.com/judge/problem/read/FENCE
"""
# O(N log N) algorithm
def solve(left: int, right: int):
    if left == right:
        return heights[left]

    mid = (left + right) // 2
    ans = max(solve(left, mid), solve(mid+1, right))

    lo, hi = mid, mid + 1
    height = min(heights[lo], heights[hi])
    ans = max(ans, height * 2)

    while left < lo or hi < right:
        if hi < right and (lo == left or heights[lo-1] < heights[hi+1]):
            hi += 1
            height = min(height, heights[hi])
        else:
            lo -= 1
            height = min(height, heights[lo])

        ans = max(ans, height * (hi - lo +1))

    return ans


# O(N) algorithm
# 진짜 미친 알고리즘. 이런거 설계할 수 있으면 진짜 좋겠다.
def solve(heights):
    heights.append(0)
    stack = []
    ret = 0

    for i in range(len(heights)):
        while stack and heights[stack[-1]] >= heights[i]:
            j = stack.pop()
            width = (i - stack[-1] - 1) if stack else i
            ret = max(ret, heights[j] * width)

        stack.append(i)

    return ret


if __name__ == '__main__':
    C = int(input())
    ans_list = []
    for _ in range(C):
        input()
        heights = [int(x) for x in input().split()]
        # ans_list.append(solve(0, len(heights)-1))
        ans_list.append(solve(heights))

    for n in ans_list:
        print(n)
