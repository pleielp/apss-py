def search(edible, chosen):
    global best

    if chosen >= best:
        return
    
    first = 0
    while first < friends_num and edible[first] > 0:
        first += 1
    
    if first == friends_num:
        best = chosen
        return

    for i in range(len(can_eat[first])):
        food = can_eat[first][i]
        for j in range(len(eaters[food])):
            edible[eaters[food][j]] += 1
        search(edible, chosen + 1)
        for j in range(len(eaters[food])):
            edible[eaters[food][j]] -= 1


case_num = int(input())
for _ in range(case_num):
    friends_num, foods_num = map(int, input().strip().split())
    friends = input().strip().split()
    edible = [0] * friends_num
    eaters = list()
    for _ in range(foods_num):
        _, *friend_names = input().strip().split()
        eaters.append(tuple(friends.index(name) for name in friend_names))
    can_eat = [[] for _ in range(friends_num)]
    for i in range(foods_num):
        for j in eaters[i]:
            can_eat[j].append(i)

    best = float('inf')
    search(edible, 0)
    print(best)