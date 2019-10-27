def inefficient_max_sum(lst):
    N = len(lst)
    ret = float('-inf')

    for i in range(N):
        for j in range(i, N):
            lst_sum = sum(lst[i:j+1])
            ret = max(ret, lst_sum)

    return ret
    

def fast_max_sum(lst):
    N = len(lst)
    ret = float('-inf')
    
    for i in range(N):
        lst_sum = 0
        for j in range(i, N):
            lst_sum += lst[j]
            ret = max(ret, lst_sum)

    return ret

if __name__ == "__main__":
    lst = [-7, 4, -3, 6, 3, -8, 3, 4]
    print(inefficient_max_sum(lst))
    print(fast_max_sum(lst))

    # 10