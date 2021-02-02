from collections import defaultdict
from collections import Counter


def flatten_lst(lst_of_lst):
    return [elm for lst in lst_of_lst for elm in lst]


# resources needed using this approach: Good job! (Max time used: 0.46/20.00, max memory used: 43761664/536870912.)
# info is a defaultdict where KEYs are point values and VALUEs are list, containing types of points having the same val
def points_coverage_by_segments(info, sorted_points):
    cnt = 0
    d = defaultdict(int)
    for p in sorted_points:
        if len(info[p]) == 1:
            if info[p][0] == 'l':
                cnt += 1
            elif info[p][0] == 'r':
                cnt -= 1
            elif info[p][0] == 'p':
                d[p] = cnt
        else:  # handle case when current point and beginning of the segments (l) and the end of segments (r) coincide
            cnt_by_types = Counter(info[p])
            cnt += cnt_by_types['l']
            if 'p' in cnt_by_types:
                d[p] = cnt
            cnt -= cnt_by_types['r']
    return d


if __name__ == '__main__':
    s, p = map(int, input().split())
    p_info = defaultdict(list)
    segments = []
    for _ in range(s):
        seg = list(map(int, input().split()))
        segments.append(seg)
        p_info[seg[0]].append('l')
        p_info[seg[1]].append('r')

    initial_points = list(map(int, input().split()))
    for p in initial_points:
        p_info[p].append('p')
    points = sorted(list(set(initial_points + flatten_lst(segments))))
    d = points_coverage_by_segments(p_info, points)

    for p in initial_points:
        print(d[p], end=' ')
