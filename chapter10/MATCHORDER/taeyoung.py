def matching(score, idx):
    for rus_player in russia:
        while True:
            if idx < len(korea):
                if korea[idx] >= rus_player:
                    score += 1
                    idx += 1
                    break
                else:
                    idx += 1
            else:
                return score

    return score


case_num = int(input())
for _ in range(case_num):
    player_num = int(input())
    russia = list(map(int, input().strip().split()))
    korea = list(map(int, input().strip().split()))
    score = 0
    idx = 0

    russia.sort()
    korea.sort()

    print(matching(score, idx))
