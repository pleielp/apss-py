

def moving_average1(weights, term):
    ret = []
    months = len(weights)
    for pivot in range(term-1, months):
        weight_sum = 0
        for gap in range(term):
            weight_sum += weights[pivot - gap]
        ret.append(round(weight_sum/term, 1))
    return ret


if __name__ == "__main__":
    print(moving_average1([4, 5, 6, 4, 8, 3], 3))
