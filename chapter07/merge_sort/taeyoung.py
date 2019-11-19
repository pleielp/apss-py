def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)
    return merge(left_array, right_array)


def merge(left, right):
    result = list()
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    result += left + right
    return result


test_list = [38, 27, 43, 9, 3, 82, 10]
print(merge_sort(test_list))
