def selection_sort(array):
    N = len(array)
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if array[min_idx] > array[j]:
                min_idx = j
        array[min_idx], array[i] = array[i], array[min_idx]


def insertion_sort(array):
    N = len(array)
    for i in range(1, N):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1


if __name__ == "__main__":
    array_test = [3, 4, 5, 1, 2, 7, 2, 1]
    selection_sort(array_test)
    print(array_test)
    array_test = [3, 4, 5, 1, 2, 7, 2, 1]
    insertion_sort(array_test)
    print(array_test)
