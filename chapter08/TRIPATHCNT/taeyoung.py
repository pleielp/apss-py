def tri_path_max(row, column):
    if row == size:
        return 0

    if cache1[row][column] == -1:
        result1 = triangle[row][column] + tri_path_max(row + 1, column)
        result2 = triangle[row][column] + tri_path_max(row + 1, column + 1)
        cache1[row][column] = max(result1, result2)

    return cache1[row][column]


def tri_path_cnt(row, column):
    if row == size - 1:
        return 1

    if cache2[row][column] == -1:
        case1 = tri_path_max(row + 1, column)
        case2 = tri_path_max(row + 1, column + 1)
        result1 = tri_path_cnt(row + 1, column) * (case1 >= case2)
        result2 = tri_path_cnt(row + 1, column + 1) * (case1 <= case2)
        cache2[row][column] = result1 + result2

    return cache2[row][column]


case_num = int(input())
for _ in range(case_num):
    size = int(input())
    triangle = [[int(char) for char in input().strip().split()] for _ in range(size)]

    cache1 = [[-1] * size for _ in range(size)]
    cache2 = [[-1] * size for _ in range(size)]
    print(tri_path_cnt(0, 0))