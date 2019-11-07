def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    lesser, greater = list(), list()
    for num in array:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
    print(1, lesser, greater)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)



test_list = [38, 27, 43, 9, 3, 82, 10, 11]
print(quick_sort(test_list))