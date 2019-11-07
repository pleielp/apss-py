def pick(n, picked, to_pick):
    if to_pick == 0:
        print(picked)

    smallest = 0 if len(picked) == 0 else picked[-1] + 1

    for next in range(smallest, n):
        picked.append(next)
        pick(n, picked, to_pick - 1)
        picked.pop()

pick(5, [], 4)