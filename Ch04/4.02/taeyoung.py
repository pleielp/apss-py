def majority2(array):
    cnt_num = 101
    cnts = [0] * cnt_num
    for value in array:
        cnts[value] += 1

    majority = 0
    for idx in range(cnt_num):
        if cnts[idx] > cnts[majority]:
            majority = idx

    return majority

print(majority2([1,1,2,3,1]))