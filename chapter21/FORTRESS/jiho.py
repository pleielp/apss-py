class TreeNode:
    def __init__(self):
        self.child = []

def solution(ramparts: list):
    X, Y, RADIUS = 0, 1, 2

    def enclose(a: int, b: int):
        if ramparts[a][RADIUS] > ramparts[b][RADIUS]:
            if (ramparts[a][X] - ramparts[b][X]) ** 2 + (
                ramparts[a][Y] - ramparts[b][Y]
            ) ** 2 < (ramparts[a][RADIUS] - ramparts[b][RADIUS]) ** 2:
                return True
        return False

    def is_child(parent, child):
        if not enclose(parent, child):
            return False

        for i in range(len(ramparts)):
            if i != parent and i != child and enclose(parent, i) and enclose(i, child):
                return False
        return True

    def get_tree(root: int):
        ret = TreeNode()
        for ch in range(len(ramparts)):
            if is_child(root, ch):
                ret.child.append(get_tree(ch))
        return ret

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

            if len(heights) > 2:
                longest = max(longest, 2 + heights[-1] + heights[-2])
            return heights[-1] + 1

        h = height(node)
        return max(longest, h)

    root_node = get_tree(0)
    return get_longest_height(root_node)


C = int(input())

for _ in range(C):
    N = int(input())
    ramparts = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        ramparts.append((x, y, r))

    print(solution(ramparts))
