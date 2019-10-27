
def inefficient_max_sum(array):
    N = len(array)
    ret = None
    for start in range(N):
        for end in range(start+1, N+1):
            max_sum = sum(array[start:end])
            if ret is None:
                ret = max_sum
            else:
                ret = max(ret, max_sum)
    return ret


def better_max_sum(array):
    N = len(array)
    ret = None
    for start in range(N):
        max_sum = 0
        for end in range(start, N):
            max_sum += array[end]
            if ret is None:
                ret = max_sum
            else:
                ret = max(ret, max_sum)
    return ret


if __name__ == "__main__":
    print(inefficient_max_sum([1, 2, 3, -3, -1, -3, 6]))
    print(better_max_sum([1, 2, 3, -3, -1, -3, 6]))
