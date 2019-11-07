def fastest_max_sum(array):
    N = len(array)
    partial_sum = 0
    ret = float('-inf')

    for i in range(N):
        partial_sum = max(partial_sum, 0) + array[i]
        ret = max(partial_sum, ret)

    return ret


input_array = [-7, 4, -3, 6, 3, -8, 3, 4]
print(fastest_max_sum(input_array))