# def solution(pattern, word, prev_char):

# case_num = int(input())
# for _ in range(case_num):
#     pattern = input()
#     # words_list = [input() for _ in range(int(input()))]
#     # print(pattern, words_list)
#     for _ in range(int(input()):
#         word = input()
#         if solution(pattern, word):
#             print(word)


def solution(p, w):
    ret = cache[p][w]
    if ret != -1:
        return ret
    
    while p < len(pattern) and w < len(word) and (pattern[p] == '?' or pattern[p] == word[w]):
        p += 1
        w += 1

    if p == len(pattern):
        # print(p, w, word)
        cache[p][w] = int(w == len(word))
        return cache[p][w]

    if pattern[p] == '*':
        for skip in range(0, len(word) - w + 1):
            if solution(p + 1, w + skip):
                cache[p][w] = 1
                return cache[p][w]


cache = [[-1] * 101 for _ in range(101)]
case_num = int(input())
for _ in range(case_num):
    pattern = input()
    # words_list = [input() for _ in range(int(input()))]
    # print(pattern, words_list)
    for _ in range(int(input())):
        word = input()
        if solution(0, 0):
            print(word)
