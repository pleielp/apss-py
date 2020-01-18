def solution(origin_preorder: list, origin_inorder: list):
    ret = []

    def print_postorder(preorder, inorder):
        n = len(preorder)
        if n == 0:
            return
        root = preorder[0]

        i = inorder.index(root)
        print_postorder(preorder[1 : i + 1], inorder[:i])
        print_postorder(preorder[i + 1 :], inorder[i + 1 :])
        ret.append(root)

    print_postorder(origin_preorder, origin_inorder)
    print(*ret)


C = int(input())

for _ in range(C):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    solution(preorder, inorder)
