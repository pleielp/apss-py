def fast_max_sum(array, lo, hi):
    if lo == hi:
        return array[lo]
    
    mid = (lo + hi) // 2
    left, right = float('-inf'), float('-inf')

    sum = 0
    for i in range(mid, lo - 1, -1):
        sum += array[i]
        left = max(left, sum)

    sum = 0
    for j in range(mid + 1, hi + 1, 1):
        sum += array[j]
        right = max(right, sum)

    single = max(fast_max_sum(array, lo, mid), fast_max_sum(array, mid + 1, hi))

    return max(left + right, single)


input_array = [-7, 4, -3, 6, 3, -8, 3, 4]
print(fast_max_sum(input_array, 0, len(input_array) - 1))