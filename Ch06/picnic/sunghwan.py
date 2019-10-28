"""Picnic code

:input:
3 
2 1 
0 1 
4 6 
0 1 1 2 2 3 3 0 0 2 1 3 
6 10 
0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5

:return:
1
3
4

url: https://algospot.com/judge/problem/read/PICNIC
"""
# First one. It passes but sucks too
def num_of_all_matched(graph):
    N = len(graph)
    matched = [0] * N
    ans = 0

    def generate_pairs(matched, first_child):
        nonlocal ans
        if all(matched):
            ans += 1
            return

        for a in range(first_child+1, N):
            if matched[a]:
                continue

            for b in range(a+1, N):
                if graph[a][b] and not matched[b]:
                    matched[a] = matched[b] = 1
                    generate_pairs(matched, a)
                    matched[a] = matched[b] = 0


    generate_pairs(matched, -1)
    return ans


# In Jongman book
def num_of_all_matched(graph):
    N = len(graph)
    matched = [0] * N
    ans = []

    def make_pair(matched):
        ret = 0

        first_free = -1
        for i in range(N):
            if not matched[i]:
                first_free = i
                break

        if first_free == -1:
            return 1

        for partner in range(first_free+1, N):
            if not matched[partner] and graph[first_free][partner]:
                matched[first_free] = matched[partner] = 1
                ret += make_pair(matched)
                matched[first_free] = matched[partner] = 0

        return ret

    return make_pair(matched)


if __name__ == "__main__":
    T = int(input())
    ans = []

    for _ in range(T):
        N, _ = (int(n) for n in input().split())
        pair_list = input().split()
        friends_graph = [[0] * N for _ in range(N)]

        i = 0
        while i < len(pair_list):
            a, b = pair_list[i:i+2]
            a, b = int(a), int(b)
            friends_graph[a][b] = 1
            friends_graph[b][a] = 1
            i += 2

        ans.append(num_of_all_matched(friends_graph))

    for n in ans:
        print(n)
