from myfunctions import measure_time

repeat_num = 10000


def fast_sum(n):
    if n == 1:
        return 1
    elif n % 2 == 1:
        return fast_sum(n - 1) + n
    return 2 * fast_sum(n // 2) + (n // 2) ** 2


def recursive_sum(n):
    if n == 1:
        return 1
    return recursive_sum(n - 1) + n


@measure_time(repeat_num=repeat_num)
def test_fast_sum(n):
    return fast_sum(n)

@measure_time(repeat_num=repeat_num)
def test_recursive_sum(n):
    return recursive_sum(n)


n = 100
print(test_fast_sum(n))
print(test_recursive_sum(n))
