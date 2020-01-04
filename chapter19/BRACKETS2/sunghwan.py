"""Tell if brackets are valid or not

url: https://algospot.com/judge/problem/read/BRACKETS2
ID : BRACKETS2
"""
RIGHT_MSG = 'YES'
WRONG_MSG = 'NO'


def is_valid_brackets(brackets):
    MAPS = {'(': ')', '{': '}', '[': ']'}
    B = len(brackets)
    stack = []

    for idx, paren in enumerate(brackets):
        if paren in MAPS.values():
            if not stack or MAPS[stack[-1]] != paren:
                return False
            else:
                stack.pop()
        else:
            stack.append(paren)
            if len(stack) > B - idx:
                return False

    return not stack


if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        parens = input()
        if is_valid_brackets(parens):
            print(RIGHT_MSG)
        else:
            print(WRONG_MSG)
