def moving_average2(array, M):
    ret = list()
    partial_sum = 0

    for value1 in array[:M - 1]:
        partial_sum += value1
    for idx, value2 in enumerate(array[M - 1:]):
        partial_sum += value2
        ret.append(partial_sum / M)
        partial_sum -= array[idx]

    return ret
