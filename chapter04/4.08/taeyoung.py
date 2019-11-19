def selection_sort(array):
    for idx in range(len(array)):
        min_index = idx
        for jdx in range(idx + 1, len(array)):
            if array[jdx] < array[min_index]:
                min_index = jdx
        array[idx], array[min_index] = array[min_index], array[idx]

    return array


def insertion_sort(array):
    for idx in range(len(array)):
        jdx = idx
        while jdx > 0 and array[jdx - 1] > array[jdx]:
            array[jdx - 1], array[jdx] = array[jdx], array[jdx - 1]
            jdx -= 1

    return array


print(selection_sort([3,2,1]))
print(insertion_sort([3,2,1]))
