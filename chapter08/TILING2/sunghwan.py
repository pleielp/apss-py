"""Get number of cases to cover board of length N

url: https://algospot.com/judge/problem/read/TILING2
ID : TILING2
"""
MAX_SIZE = 100
MOD = 1000000007

CACHE = [-1] * (MAX_SIZE + 1)
CACHE[1] = 1
CACHE[2] = 2

for i in range(3, MAX_SIZE+1):
  CACHE[i] = (CACHE[i-1] + CACHE[i-2])  % MOD

if __name__ == '__main__':
  C = int(input())
  ans = []

  for _ in range(C):
    n = int(input())
    ans.append(CACHE[n])

  for n in ans:
    print(n)
