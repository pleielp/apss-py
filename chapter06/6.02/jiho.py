def pick(n: int, picked: list, toPick: int):
    if toPick == 0:
        print(picked)
        return

    smallest = 0 if not picked else picked[-1]+1

    for next in range(smallest, n):
        picked.append(next)
        pick(n, picked, toPick - 1)
        picked.pop()
