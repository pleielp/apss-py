case_num = int(input())
for _ in range(case_num):
    team_num = int(input())
    schedules = list()
    for team_idx in range(team_num):
        schedule = tuple(map(int, input().strip().split()))
        schedules.append((schedule[:2], team_idx))
        schedules.append((schedule[2:], team_idx))

    schedules.sort(key=lambda s: s[0][1])
    print(schedules)