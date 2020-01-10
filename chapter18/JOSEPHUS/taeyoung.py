case_num = int(input())
for _ in range(case_num):
    N, K = map(int, input().strip().split())
    index = 0
    array = list(range(1, N + 1))

    while len(array) > 2:
        array.pop(index)
        index += K - 1
        index %= len(array)

    print(*array)