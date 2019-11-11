def upside_down(string):
    if string[0] == 'x':
        ret = list()
        string = string[1:]
        for i in range(4):
            if string[0] == 'x':
                piece, string = upside_down(string)
                ret.append(piece)
            else:
                ret.append(string[0])
                string = string[1:]
        ret[0], ret[1], ret[2], ret[3] = ret[2], ret[3], ret[0], ret[1]
        return 'x' + ''.join(ret), string
        
    return string, ''

case_num = int(input())
for _ in range(case_num):
    compressed = input()
    result, _ = upside_down(compressed)
    print(result)


# 책 풀이
def reverse(it):
    head = next(it)

    if head == 'b' or head == 'w':
        return head

    upper_left = reverse(it)
    upper_right = reverse(it)
    lower_left = reverse(it)
    lower_right = reverse(it)

    return 'x' + lower_left + lower_right + upper_left + upper_right


case_num = int(input())
for _ in range(case_num):
    it = iter(input())
    print(reverse(it))
