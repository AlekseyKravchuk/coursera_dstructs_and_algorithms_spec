import sys
from collections import namedtuple

Event = namedtuple('Event', ['coordinate', 'type', 'index'])


def points_cover(starts, ends, points):
    count = [None] * len(points)

    events = []
    for i in range(len(starts)):
        events.append(Event(starts[i], 'l', i))
        events.append(Event(ends[i], 'r', i))
    for i in range(len(points)):
        events.append(Event(points[i], 'p', i))

    events = sorted(events)
    number_of_segments = 0
    for e in events:
        if e.type == 'l':
            number_of_segments += 1
        elif e.type == 'r':
            number_of_segments -= 1
        elif e.type == 'p':
            count[e.index] = number_of_segments
        else:
            assert False
    return count


if __name__ == '__main__':
    data = list(map(int, ' '.join(sys.stdin.readlines()).replace('\n', '').split()))
    s, p = data[:2]
    starts, ends, points = data[2:2*s+1:2], data[3:2*s+2:2], data[2*s+2:]

    count = points_cover(starts, ends, points)
    print(*count)



