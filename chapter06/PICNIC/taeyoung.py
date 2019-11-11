# 내 풀이
def make_pairs(paired, friend_pairs):
    if len(paired) == students_num:
        return 1
    answer = 0
    for i, (student1, student2) in enumerate(friend_pairs):
        if student1 in paired or student2 in paired:
            continue
        paired.append(student1)
        paired.append(student2)
        answer += make_pairs(paired, friend_pairs[i+1:])
        paired.pop()
        paired.pop()
    return answer

case_num = int(input())
for _ in range(case_num):
    students_num, friends_pair_num = map(int, input().split())
    friends_pairs = input().split()
    friends_pairs = [friends_pairs[2 * i: 2 * i + 2] for i in range(friends_pair_num)]
    print(make_pairs(list(), friends_pairs))


# 책 풀이
def count_pairings(taken):
    first_free = -1
    for i in range(students_num):
        if not taken[i]:
            first_free = i
            break
    
    if first_free == -1:
        return 1

    ret = 0

    for pair_with in range(first_free + 1, students_num):
        if not taken[pair_with] and are_friends[first_free][pair_with]:
            taken[first_free] = taken[pair_with] = True
            ret += count_pairings(taken)
            taken[first_free] = taken[pair_with] = False

    return ret

case_num = int(input())
for _ in range(case_num):
    students_num, friends_pair_num = map(int, input().split())
    friends_pairs = input().split()
    are_friends = [[False] * students_num for _ in range(students_num)]
    for i in range(friends_pair_num):
        friend1 = int(friends_pairs[2*i])
        friend2 = int(friends_pairs[2*i+1])
        are_friends[friend1][friend2] = True
        are_friends[friend2][friend1] = True
    print(count_pairings([False] * students_num))