def post_order(tree):
    if len(tree) == 0:
        return []

    root_label = next(preordered_nodes)
    root_idx = tree.index(root_label)
    left = post_order(tree[:root_idx])
    right = post_order(tree[root_idx+1:])

    return left + right + [str(root_label)]


if __name__ == "__main__":
    case_num = int(input())
    for _ in range(case_num):
        node_num = int(input())
        preordered_nodes = map(int, input().strip().split())
        inorder_nodes = list(map(int, input().strip().split()))

        print(' '.join(post_order(inorder_nodes)))