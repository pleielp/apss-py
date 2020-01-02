# 원소 수
N = 10
explodes = [0]
def isStable(case):
    for i in range(N):
        if (case & ( 1<<i)) && (case & explodes[i]):
            return False
    return True

def count_stable_set():
    ret = 0
    sette = 1
    while sette < (1 << N):
        if not isStable(sette):
            continue
        
        canExtend = False
        for add in range(N):
            if (sette & (1 << add)) == 0 && (explodes[add] & sette) == 0:
                canExtend = True
                break
        if(not canExtend):
            ret += 1

        sette += 1
    return ret
