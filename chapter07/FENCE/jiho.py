def fence(fences):
    n = len(fences)
    if n == 0:
        return 0

    if n == 1:
        return fences[0]

    mid = n // 2
    ret = max(fence(fences[:mid]), fence(fences[mid+1:]))
    min_height = fences[mid]

    left = mid
    right = mid
    while True:
        if left == 0 and right == n-1:
            break

        if right == n-1 or fences[left-1] > fences[right+1]:
            left -= 1
            min_height = min(min_height, fences[left])

        elif left == 0 or fences[left-1] <= fences[right+1]:
            right += 1
            min_height = min(min_height, fences[right])

        area = min_height * (right - left + 1)
        ret = max(area, ret)
    return ret


C = int(input())

for _ in range(C):
    num = int(input())
    fences = list(map(int, input().split()))
    print(fence(fences))
