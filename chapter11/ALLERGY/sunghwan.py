"""Return minimum number of foods to satisfy all friends

url: https://algospot.com/judge/problem/read/ALLERGY
ID : ALLERGY
"""
from itertools import combinations


def minimum_foods(meals, FRIEND):
    M = len(meals)

    for m in range(1, M+1):
        for comb in combinations(range(M), m):
            satisfied_friends = set()

            for c in comb:
                satisfied_friends.update(meals[c])

            if len(satisfied_friends) == FRIEND:
                return m

    return -1


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        FRIEND, MEAL = (int(n) for n in input().strip().split())
        friends = list(input().strip().split())
        meals = [set() for _ in range(MEAL)]

        for meal in meals:
            satisfies = list(input().strip().split())[1:]
            for f in satisfies:
                meal.add(friends.index(f))

        ans.append(minimum_foods(meals, FRIEND))

    for n in ans:
        print(n)
