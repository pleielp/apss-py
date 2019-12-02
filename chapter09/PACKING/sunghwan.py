"""Get maximum utilities and list of items of it

url: https://algospot.com/judge/problem/read/PACKING
ID : PACKING
"""
import sys

input = sys.stdin.readline


def get_max_util_list(W, names, costs, utils):
    assert len(names) == len(costs) == len(utils)

    N = len(names)
    cache = [[-1] * (W+1) for _ in range(N)]
    chosen = []

    def pack(capacity, item):
        if item == N:
            return 0
        if cache[item][capacity] != -1:
            return cache[item][capacity]

        ret = pack(capacity, item+1)
        if capacity >= costs[item]:
            ret = max(ret, pack(capacity-costs[item], item+1) + utils[item])

        cache[item][capacity] = ret
        return ret

    def generate_item_list(capacity, item, chosen):
        if item == N:
            return
        if pack(capacity, item) == pack(capacity, item+1):
            generate_item_list(capacity, item+1, chosen)
        else:
            chosen.append(names[item])
            generate_item_list(capacity-costs[item], item+1, chosen)


    max_util = pack(W, 0)
    generate_item_list(W, 0, chosen)
    assert max_util == cache[0][W]

    return max_util, chosen


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N, W = (int(n) for n in input().strip().split())
        names = []
        costs = []
        utils = []

        for _ in range(N):
            name, cost, util = input().strip().split()
            names.append(name)
            costs.append(int(cost))
            utils.append(int(util))

        max_util, chosen = get_max_util_list(W, names, costs, utils)
        print(max_util, len(chosen))
        print('\n'.join(chosen))
