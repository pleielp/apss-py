"""Get minimum time to finish lunch time

url: https://algospot.com/judge/problem/read/LUNCHBOX
ID : LUNCHBOX
"""
from collections  import namedtuple

Lunch = namedtuple('Lunch', ['warm_up', 'eat_up'])


def min_lunch_time(warm_up_times, eat_times):
    lunches = [Lunch(w, e) for w, e in zip(warm_up_times, eat_times)]
    lunches.sort(key=lambda x: x.eat_up, reverse=True)

    ans = -float('inf')
    tmp = 0

    for lunch in lunches:
        tmp += lunch.warm_up
        if ans <= tmp + lunch.eat_up:
            ans = tmp + lunch.eat_up

    return ans


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        input()
        warm_up_times = [int(n) for n in input().split()]
        eat_times = [int(n) for n in input().split()]
        ans.append(min_lunch_time(warm_up_times, eat_times))

    for t in ans:
        print(t)
