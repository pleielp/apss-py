def solution(heights):
    heights.append(0)
    ret = 0
    remaining = []
    for idx, height in enumerate(heights):
        while remaining and heights[remaining[-1]] >= height:
            j = remaining[-1]
            remaining.pop()
            width = -1
            if not remaining:
                width = idx
            else:
                width = idx - remaining[-1] - 1
            ret = max(ret, heights[j] * width)
        remaining.append(idx)

    return ret

C = int(input())

for _ in range(C):
    input()
    heights = list(map(int, input().split()))
    print(solution(heights))
