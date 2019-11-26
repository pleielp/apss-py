def solution(board):
    n = len(board)
    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    delta = [(1,0), (1, 1)]

    def find(r, c):
        if cache[r][c] != -1:
            return cache[r][c]
        if r == n:
            return 0

        ret = 0
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            ret = max(ret, find(nr, nc))
        cache[r][c] = ret + board[r][c]
        return cache[r][c]
    
    def get_count(r, c):
        
        if r == n-1:
            return 1
        ret = 0
        sub_max = cache[r][c] - board[r][c]
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if cache[nr][nc] == sub_max:
                ret += get_count(nr, nc)
        return ret 
    find(0, 0)
    return get_count(0, 0)


C = int(input())

for _ in range(C):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(tuple(map(int, input().split())))
    
    print(solution(board))