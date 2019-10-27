def fast_max_sum(lst, low, high):
    # 구간의 길이가 1인 경우
    if low == high:
        return lst[low]

    # 배열을 lst[low ~ mid], lst[mid+1 ~ high]로 나눈다.
    mid = (low + high) // 2

    left, right = float('-inf'), float('-inf')

    # lst[i ~ mid]의 최대 구간을 찾는다.
    lst_sum = 0
    for i in range(mid, low-1, -1):
        lst_sum += lst[i]
        left = max(left, lst_sum)

    # lst[i ~ mid]의 최대 구간을 찾는다.
    lst_sum = 0
    for j in range(mid+1, high+1, 1):
        lst_sum += lst[j]
        right = max(right, lst_sum)

    # 최대 구간이 두 조각 중 하나에만 속해 있는 경우의 답을 재귀 호출로 찾는다.
    single = max(fast_max_sum(lst, low, mid), fast_max_sum(lst, mid+1, high))

    # 두 경우 중 최대치를 반환한다.
    return max(left, right, single)


if __name__ == "__main__":
    lst = [-7, 4, -3, 6, 3, -8, 3, 4]
    print(fast_max_sum(lst, 0, len(lst)-1))
