def solution(brackets):
    OPEN, CLOSE = '({[', ')}]'

    for bracket in brackets:

        if bracket in OPEN:
            stack.append(bracket)

        elif bracket in CLOSE:
            if len(stack) == 0:
                return 'NO'

            temp = stack.pop()
            if OPEN.find(temp) != CLOSE.find(bracket):
                return 'NO'

    if len(stack) != 0:
        return 'NO'
        
    return 'YES'


case_num = int(input())
for _ in range(case_num):
    brackets = input().strip()
    stack = list()
    print(solution(brackets))