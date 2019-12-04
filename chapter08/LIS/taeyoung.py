def dp1(start):
    if cache[start] == -1:
        ret = 1
        for next in range(start + 1, len(array)):
            if array[next] > array[start]:
                ret = max(ret, dp1(next) + 1)
        cache[start] = ret

    return cache[start]
            

case_num = int(input())
for _ in range(case_num):
    array_size = int(input())
    array = [int(char) for char in input().strip().split()]

    cache = [-1] * 500
    print(dp1(0))