import random


class TreapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1
        self.priority = random.random()

    def set_right(self, node):
        self.right = node
        self.calc_size()

    def set_left(self, node):
        self.left = node
        self.calc_size()

    def calc_size(self):
        self.size = 1
        if self.right:
            self.size += self.right.size
        if self.left:
            self.size += self.left.size

    def Insert(root, node):
        if root is None:
            return node
        if root.priority < node.priority:
            new_left, new_right = TreapNode.Split(root, node.value)
            node.set_left(new_left)
            node.set_right(new_right)
            return node
        elif root.value < node.value:
            root.set_right(TreapNode.Insert(root.right, node))
        else:
            root.set_left(TreapNode.Insert(root.left, node))
        return root

    def Split(root, value: int):
        if root is None:
            return (None, None)
        if root.value < value:
            new_left, new_right = TreapNode.Split(root.right, value)
            root.set_right(new_left)
            return (root, new_right)

        new_left, new_right = TreapNode.Split(root.left, value)
        root.set_left(new_right)
        return (new_left, root)

    def Merge(a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.priority < b.priority:
            b.set_left(TreapNode.Merge(a, b.left))
            return b
        else:
            a.set_right(TreapNode.Merge(a.right, b))
            return a

    def Erase(root, value):
        if root is None:
            return root

        if root.value == value:
            ret = TreapNode.Merge(root.left, root.right)
            return ret
        if value < root.value:
            root.set_left(TreapNode.Erase(root.left, value))
        else:
            root.set_right(TreapNode.Erase(root.right, value))
        return root

    def Kth(root, k):
        left_size = 0
        if root.left:
            left_size = root.left.size
        if k <= left_size:
            return TreapNode.Kth(root.left, k)
        if k == left_size + 1:
            return root
        return TreapNode.Kth(root.right, k - left_size - 1)


def solution(shifts):

    candidates = None
    for i in range(len(shifts)):
        candidates = TreapNode.Insert(candidates, TreapNode(i + 1))

    ret = [0] * len(shifts)
    i = len(shifts) - 1
    while i >= 0:
        shift = shifts[i]
        k = TreapNode.Kth(candidates, i + 1 - shift)
        ret[i] = k.value
        candidates = TreapNode.Erase(candidates, k.value)
        i -= 1
    return ret


def solution_with_array(shifts):

    ret = [0] * len(shifts)
    N = len(shifts)

    sorted_numbers = list(range(1, len(shifts) + 1))
    i = len(shifts) - 1
    while i >= 0:
        shift = shifts[i]
        value = sorted_numbers.pop(i - shift)
        ret[i] = value
        i -= 1

    return ret


C = int(input())
for _ in range(C):
    input()
    indexs = list(map(int, input().split()))
    print(*solution_with_array(indexs))

