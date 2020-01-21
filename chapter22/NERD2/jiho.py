import random
import sys


class TreapNode:
    def __init__(self, value):
        self.value = value[0]
        self.second = value[1]
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


def solution(applicants):
    root = None

    def lower_bound(node, x):
        if node.value == x:
            return node

        if node.value < x:
            if node.right:
                return lower_bound(node.right, x)
            else:
                return None
        else:
            if node.left:
                lb_node = lower_bound(node.left, x)
                if lb_node is None:
                    return node
                return lb_node
            else:
                return node

    def upper_bound(node, x):

        if node is None:
            return None

        if node.value == x:
            return node

        if node.value < x:
            if node.right:
                ub_node = upper_bound(node.right, x)
                if ub_node is None:
                    return node
                return ub_node
            else:
                return node
        else:
            if node.left:
                return upper_bound(node.left, x)
            else:
                return None

    def isDominated(x, y):
        node = lower_bound(root, x)
        if node is None:
            return False
        return y < node.second

    def removeDominatedNode(x, y):
        nonlocal root

        node = upper_bound(root, x)

        while node:
            if node.second > y:
                break
            root = TreapNode.Erase(root, node.value)
            node = upper_bound(root, x)

    def register(node):
        nonlocal root
        if root is None:
            root = node
        else:
            if isDominated(node.value, node.second):
                return root.size
            removeDominatedNode(node.value, node.second)
            root = TreapNode.Insert(root, node)

        return root.size

    ret = 0
    for p, q in applicants:
        ret += register(TreapNode((p, q)))
    return ret


C = int(input())

for _ in range(C):
    N = int(input())
    put_in = []
    for _ in range(N):
        p, q = map(int, input().split())
        put_in.append((p, q))
    print(solution(put_in))


# value_list = [10, 7, 8, 3, 5, 6, 11, 16, 15]

# root = TreapNode((1, 1))
# for v in value_list:
#     root = TreapNode.Insert(root, TreapNode((v, v)))

# def print_tree(node):
#     if not node is None:
#         print_tree(node.left)
#         print(node.value)
#         print_tree(node.right)

