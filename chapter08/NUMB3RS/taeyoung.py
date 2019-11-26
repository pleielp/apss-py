def next_day(possibilities):
    new_possibilities = [0] * town_num
    for i in range(town_num):
        for j in town_conn_idx[i]:
            if town_conn[i][j] == 1:
                new_possibilities[j] += possibilities[i] / cases[i]
    return new_possibilities



case_num = int(input())
for _ in range(case_num):
    town_num, days, prison = map(int, input().strip().split())
    town_conn = [[int(char) for char in input().strip().split()] for _ in range(town_num)]
    town_conn_idx = [[jdx for jdx, conn in enumerate(conns) if conn == 1] for conns in town_conn]
    input()
    result_town = map(int, input().strip().split())
    
    possibilities = [0] * town_num
    possibilities[prison] = 1
    cases = tuple(sum(case) for case in town_conn)

    for _ in range(days):
        possibilities = next_day(possibilities)

    print(' '.join(str(possibilities[idx]) for idx in result_town))