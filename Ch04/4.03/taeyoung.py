def moving_average1(array, M):
    ret = list()

    for i in range(M - 1, len(array)):
        partial_sum = 0
        for j in range(0, M):
            partial_sum += array[i - j]
        ret.append(partial_sum / M)

    return ret
