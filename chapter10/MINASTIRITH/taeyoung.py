from math import atan2, asin, pi


def coord_to_angle(y, x, r):
    angle_center = (atan2(y, x) + 2 * pi) % (2 * pi)
    angle_range = asin((r / 2) / 8)
    start = angle_center - 2 * angle_range
    end = angle_center + 2 * angle_range

    return start, end


def fill_wall(begin, last):
    ret = 0
    idx = 0

    while begin < last:
        max_cover = -1
        while idx < len(angles) and angles[idx][0] <= begin:
            max_cover = max(max_cover, angles[idx][1])
            idx += 1

        if max_cover <= begin:
            return float('inf')

        begin = max_cover
        ret += 1

    return ret


case_num = int(input())
for _ in range(case_num):
    angles = list()

    cp_num = int(input())
    for _ in range(cp_num):

        y, x, r = map(float, input().strip().split())
        angles.append(coord_to_angle(y, x, r))
    
    angles.sort()
    # inits = [(start, end) for start, end in angles if start < -pi < end]
    # angles = angles[len(inits):]
    ans = float('inf')
    for i in range(len(angles)):
        if angles[i][0] <= 0 or angles[i][1] >= 2 * pi:
            begin = angles[i][1] % (2 * pi)
            end = (angles[i][0] + 2 * pi) % (2 * pi)
            ans = min(ans, 1 + fill_wall(begin, end))
        
    # for start, end in inits:
    #     ans = min(ans, fill_wall(start + 2 * pi, end))

    print('IMPOSSIBLE' if ans == float('inf') else ans)
# from math import atan2, asin, pi


# def coord_to_angle(y, x, r):
#     angle_center = atan2(y, x)
#     angle_range = asin((r / 2) / 8)
#     start = angle_center - 2 * angle_range
#     end = angle_center + 2 * angle_range
#     if end > pi:
#         start -= 2 * pi
#         end -= 2 * pi

#     return start, end


# def fill_wall(last, begin):
#     ret = 1
#     idx = 0

#     while begin < last:
#         max_cover = -pi
#         while idx < len(angles) and angles[idx][0] <= begin:
#             max_cover = max(max_cover, angles[idx][1])
#             idx += 1

#         if max_cover <= begin:
#             return float('inf')

#         begin = max_cover
#         ret += 1

#     return ret


# case_num = int(input())
# for _ in range(case_num):
#     angles = list()

#     cp_num = int(input())
#     for _ in range(cp_num):

#         y, x, r = map(float, input().strip().split())
#         angles.append(coord_to_angle(y, x, r))
    
#     angles.sort()
#     inits = [(start, end) for start, end in angles if start < -pi < end]
#     angles = angles[len(inits):]
#     ans = float('inf')

#     for start, end in inits:
#         ans = min(ans, fill_wall(start + 2 * pi, end))

#     print('IMPOSSIBLE' if ans == float('inf') else ans)