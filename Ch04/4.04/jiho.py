def moving_average2(weights, term):
    months = len(weights)
    weight_sum = sum([weights[i] for i in range(term)])
    ret = [weight_sum/term]
    for pivot in range(term, months):
        weight_sum += weights[pivot]
        weight_sum -= weights[pivot-term]
        ret.append(weight_sum/term)
    return ret


if __name__ == "__main__":
    print(moving_average2([4, 5, 6, 4, 8, 3], 3))
