def majority1(array):
    majority_count = 0
    majority = -1
    for value in array:
        count = 0
        for target in array:
            if target == value:
                count += 1
        if majority_count < count:
            majority_count = count
            majority = value
    return majority


if __name__ == "__main__":
    print(majority1([1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4, 5, 5]))
