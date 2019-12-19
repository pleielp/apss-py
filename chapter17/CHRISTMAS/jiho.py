from collections import Counter

MOD = 20091101
def solution(boxs, child):
    def get_psum(array):
        ret = [0] * len(array)
        ret[0] = array[0]
        for i in range(1, len(array)):
            ret[i] = ret[i - 1] + array[i]
        return ret

    psum_boxs = get_psum(boxs)
    psum_boxs_moded = list(map(lambda x: x % child, psum_boxs))
    psum_boxs_moded.append(0)

    def find_orders():
        counter = Counter(psum_boxs_moded)
        ret = 0
        for key, value in counter.items():
            ret += ((value) * (value - 1) // 2) % MOD
        return ret % MOD

    cache = [-1] * (len(boxs) + 1)

    def find_max_order(idx):

        if idx == len(boxs):
            return 0

        if cache[idx] != -1:
            print(idx)
            return cache[idx]

        ret = 0

        if idx != -1:
            if boxs[idx] % child == 0:
                ret = max(ret, find_max_order(idx + 1) + 1)

        for i in range(idx + 1, len(boxs)):
            if psum_boxs_moded[i] == psum_boxs_moded[idx]:
                ret = max(ret, find_max_order(i + 1) + 1)
                break
        ret = max(ret, find_max_order(idx + 1))

        cache[idx] = ret
        return ret

    order_count = find_orders()
    max_order_count = find_max_order(-1)
    print(str(order_count) + " " + str(max_order_count))


C = int(input())
for _ in range(C):
    N, K = map(int, input().split())
    boxs = list(map(int, input().split()))
    solution(boxs, K)
