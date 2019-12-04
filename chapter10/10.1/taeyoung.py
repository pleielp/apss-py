def schedule(begin, end):
    order = list(zip(begin, end))
    order.sort(key= lambda pair: pair[1])

    earliest = 0
    selected = 0

    for pair in order:
        if pair[1] > earliest and pair[0] >= earliest:
            earliest = pair[1]
            selected += 1

    return selected


begin = [1, 1, 2, 2, 2, 3, 5, 6, 8, 8, 9]
end = [4, 7, 4, 7, 4, 5, 9, 9, 10, 9, 10]
print(schedule(begin, end))