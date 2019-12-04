case_num = int(input())
for _ in range(case_num):
    box_num = int(input())
    heat_times = list(map(int, input().strip().split()))
    eat_times = list(map(int, input().strip().split()))

    times = list(zip(eat_times, heat_times))
    times.sort(reverse=True)

    heat_accum = 0
    ret = 0
    for eat_time, heat_time in times:
        heat_accum += heat_time
        ret = max(ret, heat_accum + eat_time)

    print(ret)

