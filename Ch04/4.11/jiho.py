def fastest_max_sum(array):
    ret = float("-inf")
    psum = float("-inf")
    for idx in range(len(array)):
        psum = max(psum, 0) + array[idx]
        ret = max(psum, ret)
    return ret


if __name__ == "__main__":
    print(fastest_max_sum([1, 2, 3, -3, -1, -3, 6]))
