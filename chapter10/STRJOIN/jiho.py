import heapq
def solution(sizes):
    heapq.heapify(sizes)
    ret = 0
    while len(sizes) > 1:
        src, dest = heapq.heappop(sizes), heapq.heappop(sizes)
        merge = src + dest
        ret += merge
        heapq.heappush(sizes, merge)
    return ret



C = int(input())
for _ in range(C):
    _ = input()
    str_sizes = list(map(int, input().split()))
    print(solution(str_sizes))