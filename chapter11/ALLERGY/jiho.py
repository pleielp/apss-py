def solution(food_edible_freinds, friend_num):

    friend_edible_foods = []
    for friend in range(friend_num):
        food_list = []
        for food, friends in enumerate(food_edible_freinds):
            if friend in friends:
                food_list.append(food)
        friend_edible_foods.append(food_list)

    friend_food_count = [0 for _ in range(friend_num)]

    def set_eat_able(friends):
        for friend in friends:
            friend_food_count[friend] += 1

    def unset_eat_able(friends):
        for friend in friends:
            friend_food_count[friend] -= 1

    best = float("inf")

    def search(chosen):

        nonlocal best
        if chosen >= best:
            return

        first = 0
        while first < friend_num and friend_food_count[first] > 0:
            first += 1

        if first == friend_num:
            best = chosen
            return

        for food in friend_edible_foods[first]:
            set_eat_able(food_edible_freinds[food])
            search(chosen + 1)
            unset_eat_able(food_edible_freinds[food])

    search(0)
    return best


C = int(input())

for _ in range(C):
    n, m = map(int, input().split())
    friend_names = input().split()
    foods = []
    for _ in range(m):
        names = input().split()[1:]
        index_of_names = tuple(map(lambda name: friend_names.index(name), names))
        foods.append(index_of_names)

    print(solution(foods, len(friend_names)))

