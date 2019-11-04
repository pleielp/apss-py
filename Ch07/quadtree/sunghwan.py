"""Return reversed quadtree string up and down

url: https://algospot.com/judge/problem/read/QUADTREE
ID : QUADTREE
"""
def reverse_quadtree(quad):
    i = 0

    def divide_and_merge():
        nonlocal i
        if quad[i:] in 'wb':
            return quad[i:]
        elif 'x' not in quad[i:i+4]:
            p1, p2, p3, p4 = quad[i:i+4]
            i += 4
            return p3 + p4 + p1 + p2

        parts = []
        if quad[i] == 'x':
            i += 1
            while len(parts) < 4:
                if quad[i] in 'wb':
                    parts.append(quad[i])
                    i += 1
                else:
                    parts.append(divide_and_merge())
            return 'x' + parts[2] + parts[3] + parts[0] + parts[1]

    return divide_and_merge()


if __name__ == '__main__':
    T = int(input())
    ans = []

    for _ in range(T):
        ans.append(reverse_quadtree(input()))

    for strng in ans:
        print(strng)
