import heapq
def solution(boxs):
    boxs = [(-e, m) for m, e in boxs]
    heapq.heapify(boxs)
    sum_micro = 0
    ret = 0
    while boxs:
        eat, micro = heapq.heappop(boxs)
        sum_micro += micro
        ret = max(ret, sum_micro - eat)
    return ret

C = int(input())
for _ in range(C):
    input()
    micro_time = list(map(int, input().split()))
    eat_time = list(map(int, input().split()))
    boxs = list(zip(micro_time, eat_time))
    print(solution(boxs))