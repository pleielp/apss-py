

def solution(compressed):
    compressed = iter(compressed)

    def quadtree(compressed_iter):
        char = next(compressed_iter)
        if char != 'x':
            return char

        nw = quadtree(compressed_iter)
        ne = quadtree(compressed_iter)
        sw = quadtree(compressed_iter)
        se = quadtree(compressed_iter)

        return 'x' + sw + se + nw + ne
    return quadtree(compressed)


c = int(input())

for _ in range(c):
    compressed = input()
    print(solution(compressed))
