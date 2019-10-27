def majority2(array):
    count = [0] * len(array)
    for value in array:
        count[value] += 1
    return count.index(max(count))


if __name__ == "__main__":
    result = majority2([1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 8, 9])
    assert result == 3
    print(result)
