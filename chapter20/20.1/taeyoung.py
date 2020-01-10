def naive_search(H, N):
    ret = list()

    for begin in range(len(H) - len(N) + 1):
        matched = True
        for i in range(len(N)):
            if H[begin + i] != N[i]:
                matched = False
                break
        if matched:
            ret.append(begin)

    return ret


print(naive_search('avadakedavra', 'aked'))
print(naive_search('aked', 'avadakedavra'))