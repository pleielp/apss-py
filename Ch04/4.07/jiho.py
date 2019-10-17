
def first_index(array, element):
    for idx, item in enumerate(array):
        if item == element:
            return idx
    return -1


if __name__ == "__main__":
    assert 5 == first_index([1, 2, 3, 4, 5, 6], 6)
