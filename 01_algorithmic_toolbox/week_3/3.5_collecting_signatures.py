from collections import namedtuple


def min_points(s):  #function takes the list of segments, each of them is namedtuple('Segment', ['start', 'end'])
    curr = 0  # current index of segment
    second_last = len(s) - 2  # index of second last segment
    last = len(s) - 1  # index of last segment
    points = []
    while curr <= last:
        m = s[curr].end
        while curr <= second_last and s[curr+1].start <= m:
            if s[curr + 1].end < m:
                m = s[curr + 1].end
            curr += 1

        points.append(m)
        curr += 1

    print(len(points))
    for point in points:
        print(point, end=' ')


def main():
    Segment = namedtuple('Segment', ['start', 'end'])
    segments = sorted([Segment(*(map(int, input().split()))) for _ in range(int(input()))], key=lambda x: x[0])
    # print(segments)
    min_points(segments)


if __name__ == '__main__':
    main()
