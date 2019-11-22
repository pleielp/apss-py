def solution(A, B):
    cache = [[-1 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
    def jlis(idx_a, idx_b):

        if cache[idx_a+1][idx_b+1] != -1:
            return cache[idx_a+1][idx_b+1]
        ret = 2
        a = float("-inf") if idx_a == -1 else A[idx_a]
        b = float("-inf") if idx_b == -1 else B[idx_b]

        max_element = max(a, b)

        for nextA in range(idx_a+1, len(A)):
            if max_element < A[nextA]:
                ret = max(ret, jlis(nextA, idx_b) + 1)
        for nextB in range(idx_b+1, len(B)):
            if max_element < B[nextB]:
                ret = max(ret, jlis(idx_a, nextB) + 1)
        cache[idx_a+1][idx_b+1] = ret
        return ret
    return jlis(-1, -1) - 2


if __name__ == "__main__":
    C = int(input())
    for _ in range(C):
        input()
        lis_A = list(map(int, input().split()))
        lis_B = list(map(int, input().split()))
        print(solution(lis_A, lis_B))
