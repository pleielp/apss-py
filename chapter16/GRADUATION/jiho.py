def get_bit(nums):
    result = 0
    for num in nums:
        result |= 1 << num
    return result


def bit_count(bits):
    return bin(bits).count("1")


def solution(satified_count, limit_per_semester, prerequisites, classes_per_semester):
    N = len(prerequisites)
    cache = [[-1 for _ in range(1 << N)] for _ in range(10)]
    ret = float("inf")

    prerequisites = [get_bit(prerequisite) for prerequisite in prerequisites]
    classes_per_semester = [get_bit(classes) for classes in classes_per_semester]

    def minsemester(semester, taken):

        if cache[semester][taken] != -1:
            return cache[semester][taken]

        if bit_count(taken) >= satified_count:
            return 0

        if semester == len(classes_per_semester):
            return float("inf")

        ret = float("inf")

        canTake = classes_per_semester[semester] & ~taken
        i = 0
        while i < N:
            if canTake & (1 << i) and (taken & prerequisites[i]) != prerequisites[i]:
                canTake = canTake & ~(1 << i)
            i += 1
        take = canTake

        while take > 0:
            if bit_count(take) > limit_per_semester:
                take = (take - 1) & canTake
                continue

            ret = min(ret, minsemester(semester + 1, taken | take) + 1)

            take = (take - 1) & canTake
        ret = min(ret, minsemester(semester + 1, taken))

        cache[semester][taken] = ret
        return ret

    return minsemester(0, 0)


C = int(input())

for _ in range(C):
    N, K, M, L = map(int, input().split())
    # N : 전공과목수, K: 들어야할 과목의 수, M: 학기의 수
    # L: 한 학기에 들을 수 있는 과목의 수

    required_subject = []
    for n in range(N):
        _, *subjects = map(int, input().split())
        required_subject.append(subjects)

    semester_subjects = []
    for m in range(M):
        _, *subjects = map(int, input().split())
        semester_subjects.append(subjects)

    result = solution(K, L, required_subject, semester_subjects)
    print(result if result != float("inf") else "IMPOSSIBLE")

