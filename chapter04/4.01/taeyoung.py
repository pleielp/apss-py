def majority1(array):
    majority, majority_cnt = -1, 0

    for value1 in array:
        cnt = 0
        for value2 in array:
            if value2 == value1:
                cnt += 1
        if cnt > majority_cnt:
            majority_cnt = cnt
            majority = value1

    return majority
