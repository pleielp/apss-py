class TreeNode:
    def __init__(self):
        self.child = []


def solution(ramparts: list):
    X, Y, RADIUS = 0, 1, 2
    nodes = [TreeNode() for _ in range(len(ramparts))]

    def enclose(a: int, b: int):
        if (
            ramparts[a][RADIUS] > ramparts[b][RADIUS]
            and (ramparts[a][X] - ramparts[b][X]) ** 2
            + (ramparts[a][Y] - ramparts[b][Y]) ** 2
            < (ramparts[a][RADIUS] - ramparts[b][RADIUS]) ** 2
        ):
            return True
        return False

    def is_child(parent, child):
        return enclose(parent, child)

    def make_tree():
        for ch in range(len(ramparts)):
            for parent in range(ch + 1, len(ramparts)):
                if is_child(parent, ch):
                    nodes[parent].child.append(nodes[ch])
                    break

    def get_longest_height(node):
        longest = 0

        def height(root):
            nonlocal longest
            heights = []
            for ch in root.child:
                heights.append(height(ch))
            if len(heights) == 0:
                return 0

            heights.sort()

            if len(heights) >= 2:
                longest = max(longest, 2 + heights[-1] + heights[-2])
            return heights[-1] + 1

        h = height(node)
        return max(longest, h)

    make_tree()
    return get_longest_height(nodes[len(ramparts) - 1])


C = int(input())

for _ in range(C):
    N = int(input())
    ramparts = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        ramparts.append((x, y, r))
    ramparts.sort(key=lambda x: x[2])
    print(solution(ramparts))
