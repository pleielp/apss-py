def set_bit(nums):
    result = 0
    for num in nums:
        result |= (1 << num)
    return result


def bit_count(bits):
    return bin(bits).count('1')

def solution(required_count, limit_per_semeter, prerequisites, subjects_per_semeter):
    ret = float('inf')
    N = len(prerequisites) # 과목 수
    
    prerequisites = [ set_bit(prerequisite)  for prerequisite in prerequisites]
    subjects_per_semeter = [ set_bit(subjects) for subjects in subjects_per_semeter ]
    
    def minSemeter(semeter, taken):
        if bit_count(taken) >= required_count:
            return 0
        
        if semeter == len(subjects_per_semeter):
            return float('inf')
        
        ret = float('inf')

        canTake = (subjects_per_semeter[semeter] & ~taken)
        i = 0
        while i < N:
            if canTake & (1 << i) and (taken & prerequisites[i]) != prerequisites[i]:
                canTake = canTake & ~(1 << i)
            i += 1
        take = canTake

        while take > 0:
            if bit_count(take) > limit_per_semeter:
                take = (take - 1) & canTake
                continue
            
            ret = min(ret, minSemeter(semeter + 1, taken | take) + 1)

            take = (take - 1) & canTake
        ret = min(ret, minSemeter(semeter + 1, taken))
        return ret

    return minSemeter(0, 0)
            
                
C = int(input())

for _ in range(C):
    N, K, M, L = map(int, input().split())
    # N : 전공과목수, K: 들어야할 과목의 수, M: 학기의 수
    # L: 한학기에 들을 수 있는 과목의 수
    
    required_subject = []
    for n in range(N):
        _, *subjects = map(int, input().split())
        required_subject.append(subjects)
        
    
    semester_subjects = []
    for m in range(M):
        _, *subjects = map(int, input().split())
        semester_subjects.append(subjects)

    result = solution(K, L, required_subject, semester_subjects)
    print( result if result != float('inf') else 'IMPOSSIBLE')