def fastest_max_sum(lst):
    N = len(lst)
    ret = float('-inf')
    psum = 0
    for i in range(N):
        psum = max(psum, 0) + lst[i]
        ret = max(psum, ret)
    
    return ret

if __name__ == "__main__":
    lst = [-7, 4, -3, 6, 3, -8, 3, 4]
    print(fastest_max_sum(lst))