"""Last two men standing

url: https://algospot.com/judge/problem/read/JOSEPHUS
ID : JOSEPHUS
"""
def josephus(N, STRIDE, idx_start_from_1=True):
    still_alive = list(range(N))
    kill = 0

    while len(still_alive) > 2:
        still_alive.pop(kill)
        kill = (kill + STRIDE - 1) % len(still_alive)

    if idx_start_from_1:
        return [n + 1 for n in still_alive]
    else:
        return still_alive


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        N, STRIDE = (int(n) for n in input().split())
        ans.append(josephus(N, STRIDE, idx_start_from_1=True))

    for a, b in ans:
        print(a, b)
