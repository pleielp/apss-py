def solution(brackets):
    CLOSE_BRACKETS = [")", "}", "]"]
    OPEN_BRACKETS = ["(", "{", "["]
    stack = []
    for bracket in brackets:
        if bracket in CLOSE_BRACKETS:
            if stack and OPEN_BRACKETS.index(stack[-1]) == CLOSE_BRACKETS.index(
                bracket
            ):
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)
    if stack:
        return False
    return True


C = int(input())
for _ in range(C):
    brackets = input()
    print("YES" if solution(brackets) else "NO")
