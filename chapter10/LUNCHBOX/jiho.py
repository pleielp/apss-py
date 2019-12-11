import heapq
def solution(boxs):
    boxes = [(-e, m) for m, e in boxes]
    heapq.heapify(boxs)
    sum_micro = 0
    ret = 0
    while boxes:
        eat, micro = heapq.heappop(boxes)
        sum_micro += micro
        ret = max(ret, sum_micro - eat)
    return ret

C = int(input())
for _ in range(C):
    input()
    micro_time = list(map(int, input().split()))
    eat_time = list(map(int, input().split()))
    boxes = list(zip(micro_time, eat_time))
    print(solution(boxes))
