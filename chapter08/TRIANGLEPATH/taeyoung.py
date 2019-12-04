def dp1(row, column, sum):
    if row == size:
        return sum

    sum += triangle[row][column]
    if cache[row][column] == -1:
        cache[row][column] = sum

    result1 = dp1(row + 1, column, sum)
    result2 = dp1(row + 1, column + 1, sum)

    return max(result1, result2)


def dp2(row, column):
    if row == size:
        return 0

    if cache[row][column] == -1:
        result1 = triangle[row][column] + dp2(row + 1, column)
        result2 = triangle[row][column] + dp2(row + 1, column + 1)
        cache[row][column] = max(result1, result2)

    return cache[row][column]



case_num = int(input())
for _ in range(case_num):
    size = int(input())
    triangle = [[int(char) for char in input().strip().split()] for _ in range(size)]

    # 무식한 방법
    cache = [[-1] * size for _ in range(size)]
    print(dp1(0, 0, 0))

    # 입력 걸러낸 방법
    cache = [[-1] * size for _ in range(size)]
    print(dp2(0, 0))