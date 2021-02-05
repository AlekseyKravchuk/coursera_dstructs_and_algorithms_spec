import sys
from collections import namedtuple
from bisect import bisect_left, bisect_right

Event = namedtuple('Event', ['coordinate', 'type', 'index'])


def point_coverage(starts, ends, points):
    counts = [None] * len(points)
    num_of_segments = 0
    events = []

    for i in range(len(starts)):
        events.append(Event(starts[i], 'l', i))
        events.append(Event(ends[i], 'r', i))
    for i in range(len(points)):
        events.append(Event(points[i], 'p', i))
    events.sort()

    # scanning from left to right
    for e in events:
        if e.type == 'l':
            num_of_segments += 1
        elif e.type == 'r':
            num_of_segments -= 1
        elif e.type == 'p':
            counts[e.index] = num_of_segments
    return counts

# Resource consumption: Max time used: 0.15/20.00, max memory used: 26198016/536870912
def point_coverage_using_binary_search(starts, ends, points):
    num_of_segments = len(starts)              # this is equivalent to len(ends)
    counts = [num_of_segments] * len(points)   # array to store counts, pre-initialized with num_of_segments

    starts, ends = sorted(starts), sorted(ends)

    # for each point: cover(p) = num_of_segments - (leftwards + rightwards)
    for i, coord in enumerate(points):
        leftwards = bisect_left(ends, coord)                    # leftwards - num of segment right-ends BEFORE point
        rightwards = num_of_segments - bisect_right(starts, coord)  # rightwards - num of segment left-ends AFTER point
        counts[i] -= (leftwards + rightwards)
    return counts


if __name__ == '__main__':
    data = list(map(int, ' '.join(sys.stdin.readlines()).replace('\n', '').split()))
    s, p = data[:2]
    starts, ends, points = data[2:s * 2 + 1:2], data[3:s * 2 + 2:2], data[s * 2 + 2:]

    # print(*point_coverage(starts, ends, points))
    print(*point_coverage_using_binary_search(starts, ends, points))
