from functools import reduce

def solution(numbers, quantize_n):
    numbers = sorted(numbers)
    cache = [[-1 for _ in range(quantize_n + 1)] for _ in range(len(numbers)+1)]

    sub_sums = [0] * len(numbers)
    sub_sq_sums = [0] * len(numbers)
    sub_sum = 0
    sub_sq_sum = 0
    for idx, number in enumerate(numbers):
        sub_sum += number
        sub_sq_sum += number ** 2
        sub_sums[idx] = sub_sum
        sub_sq_sums[idx] = sub_sq_sum

    def sum_error_square(start_idx, end_idx):
        
        n = end_idx - start_idx
        if start_idx > 0:
            sub_sum = sub_sums[end_idx - 1] - sub_sums[start_idx - 1] 
            sub_sq_sum = sub_sq_sums[end_idx - 1] - sub_sq_sums[start_idx - 1]
        else:
            sub_sum = sub_sums[end_idx -1]
            sub_sq_sum = sub_sq_sums[end_idx - 1]
        
        average = round(sub_sum / n)
        return n * (average ** 2) + sub_sq_sum - 2 * average * sub_sum

    def quantize(start_idx, kind):
        if cache[start_idx][kind] != -1:
            return cache[start_idx][kind]

        if start_idx == len(numbers):
            return 0
        
        if kind == 0:
            return float('inf')

        ret = float('inf')

        for end_idx in range(start_idx + 1, len(numbers) + 1):
            ret = min(ret, sum_error_square(start_idx, end_idx) + quantize(end_idx, kind - 1))

        cache[start_idx][kind] = ret

        return ret

    return quantize(0, quantize_n)


C = int(input())
for _ in range(C):
    _, s = tuple(map(int, input().split()))
    numbers = list(map(int, input().split()))
    print(solution(numbers, s))