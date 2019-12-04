import heapq

case_num = int(input())
for _ in range(case_num):
    string_num = int(input())
    lengths = list(map(int, input().strip().split()))

    heapq.heapify(lengths)
    cost = 0

    while len(lengths) > 1:
        str1 = heapq.heappop(lengths)
        str2 = heapq.heappop(lengths)
        cost += str1 + str2
        heapq.heappush(lengths, str1 + str2)

    print(cost)