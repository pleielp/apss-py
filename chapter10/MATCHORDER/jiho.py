
def solution(russians:list, koreans:list):
    BEST_RATING = -1
    WORST_RATING = 0

    russians.sort()
    koreans.sort()
    win_count = 0

    def get_lower_bound(lo, hi):
        while lo < hi:
            mid = (hi + lo) // 2
            if koreans[mid] >= russians[BEST_RATING]:
                hi = mid
            else:
                lo = mid + 1
        return hi

    while russians:
        if russians[BEST_RATING] > koreans[BEST_RATING]:
            koreans.pop(WORST_RATING)
        else:
            least_rating_korean = get_lower_bound(0, len(koreans)-1)
            koreans.pop(least_rating_korean)
            win_count += 1
        russians.pop(BEST_RATING)
    return win_count

C = int(input())

for _ in range(C):
    _  = input()
    russians = list(map(int, input().split()))
    koreans =  list(map(int, input().split()))
    print(solution(russians, koreans))