class Wall(object):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.childs = list()
    
    def __repr__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.r)


def is_child(wall_1, wall_2):
    if (wall_1.x - wall_2.x) ** 2 + (wall_1.y - wall_2.y) ** 2 > (wall_1.r + wall_2.r) ** 2:
        return False

    return True


def max_passing_through(root):
    if len(root.childs) == 0:
        return 0
    
    ret = list()
    for child in root.childs:
        ret.append(max_passing_through(child) + 1)

    ret.sort(reverse=True)
    if len(ret) > 1:
        cands.append(sum(ret[:2]))

    return ret[0]


if __name__ == "__main__":
    X, Y, R = 0, 1, 2
    case_num = int(input())
    for _ in range(case_num):
        walls_num = int(input())
        walls = [Wall(*map(int, input().strip().split())) for _ in range(walls_num)]
        walls.sort(key=lambda wall:wall.r)

        for i, wall_1 in enumerate(walls):
            for wall_2 in walls[i+1:]:
                if is_child(wall_1, wall_2):
                    wall_2.childs.append(wall_1)
                    break

        root = walls[-1]

        cands = list()
        cands.append(max_passing_through(root))
        print(max(cands))