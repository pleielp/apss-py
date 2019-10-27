def inefficient_max_sum(array):
    N = len(array)
    ret = float('-inf')

    for i in range(N):
        for j in range(i, N):
            partial_sum = sum(array[i:j + 1])
            ret = max(ret, partial_sum)

    return ret


def better_max_sum(array):
    N = len(array)
    ret = float('-inf')

    for i in range(N):
        partial_sum = 0
        for j in range(i, N):
            partial_sum += array[j] 
            ret = max(ret, partial_sum)
    
    return ret


input_array = [-7, 4, -3, 6, 3, -8, 3, 4]
print(inefficient_max_sum(input_array))
print(better_max_sum(input_array))