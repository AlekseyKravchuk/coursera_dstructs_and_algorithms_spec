from collections import defaultdict
from collections import Counter
import timeit


def read_segments(segments_num):
    coord_type_map = defaultdict(list)
    for _ in range(segments_num):
        l, r = map(int, input().split())
        coord_type_map[l].append('l')
        coord_type_map[r].append('r')
    return coord_type_map


def read_points(coord_type_map):
    points = list(map(int, input().split()))
    for coord in points:
        coord_type_map[coord].append('p')
    return points


def points_coverage_by_segments(coord_type_map, points):
    cntr_dict = defaultdict(int)
    points = sorted(points)

    # scanning sorted points from left to right
    cnt = 0
    for coord in sorted(list(coord_type_map.keys())):
        if len(coord_type_map[coord]) == 1:
            if coord_type_map[coord][0] == 'l':
                cnt += 1
            elif coord_type_map[coord][0] == 'r':
                cnt -= 1
            elif coord_type_map[coord][0] == 'p':
                cntr_dict[coord] = cnt
        else:  # handle case when current point and beginning of the segments (l) and the end of segments (r) coincide
            cnt_by_types = Counter(coord_type_map[coord])
            cnt += cnt_by_types['l']
            if 'p' in cnt_by_types:
                cntr_dict[coord] = cnt
            cnt -= cnt_by_types['r']
    return cntr_dict


if __name__ == '__main__':
    s, p = map(int, input().split())
    coord_type_map = read_segments(s)
    points = read_points(coord_type_map)

    d = points_coverage_by_segments(coord_type_map, points[:])

    for coord in points:
        print(d[coord], end=' ')
