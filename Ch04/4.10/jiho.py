def solution(array):
    def fastMaxsum(lo, hi):
        if lo == hi:
            return lo
        mid = (lo + hi) // 2

        # lo ~ mid
        left_max_sum = float("-inf")
        max_sum = 0
        for idx in range(mid, lo-1, -1):
            max_sum += array[idx]
            left_max_sum = max(left_max_sum, max_sum)

        # mid+1 ~ hi
        right_max_sum = float("-inf")
        max_sum = 0
        for idx in range(mid+1, hi+1):
            max_sum += array[idx]
            right_max_sum = max(right_max_sum, max_sum)

        between_max_sum = left_max_sum + right_max_sum

        single = max(fastMaxsum(lo, mid), fastMaxsum(mid+1, hi))
        print(between_max_sum, single)
        return max(between_max_sum, single)

    return fastMaxsum(0, len(array)-1)


if __name__ == "__main__":
    print(solution([1, 2, 3, -3, -1, -3, 6]))
