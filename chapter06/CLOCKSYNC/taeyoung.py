from itertools import product


switches = ((0, 1, 2),
            (3, 7, 9, 11),
            (4, 10, 14, 15),
            (0, 4, 5, 6, 7),
            (6, 7, 8, 10, 12),
            (0, 2, 14, 15),
            (3, 14, 15),
            (4, 5, 7, 14, 15),
            (1, 2, 3, 4, 5),
            (3, 4, 5, 9, 13))


case_num = int(input())
for _ in range(case_num):
    clocks = list(map(int, input().strip().split()))

    ret = float('inf')
    switch_combs = product(range(4), repeat=10)
    for i, switch_comb in enumerate(switch_combs):
        new_clocks = list(clocks)
        for switch_idx, switch_num in enumerate(switch_comb):
            for x in switches[switch_idx]:
                new_clocks[x] += 3 * switch_num
        for y in range(len(new_clocks)):
            new_clocks[y] = new_clocks[y] % 12
        if not any(new_clocks):
            ret = min(ret, sum(switch_comb))

    print(ret)

