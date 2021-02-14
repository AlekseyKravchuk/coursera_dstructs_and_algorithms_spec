from collections import namedtuple
from math import inf
from math import sqrt
import random

Point = namedtuple('Point', ['x', 'y'])


def euclidean_dist(p1, p2):
    return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def min_dist_brute_force(points):
    min_dist = inf
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_dist(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist


def closest_split_dist(X, Y, median, min_dist):
    # Create a subarray of points not further than min_dist_over_halves from median in x-sorted array
    # Now these points will be sorted by Y coordinate
    strip = [point for point in Y if abs(point.x - median) < min_dist]
    for i, curr_point in enumerate(strip):
        for j in range(i + 1, min(i + 6, len(strip))):
            if strip[j].y - curr_point.y < min_dist:
                dist = euclidean_dist(curr_point, strip[j])
                if dist < min_dist:
                    min_dist = dist
            else:
                break
    return min(min_dist, min_dist)


def closest_dist(X, Y):
    if len(X) <= 3:
        return min_dist_brute_force(X)

    mid = len(X) // 2  # индекс медианы по оси X
    median = X[mid].x  # медиана по оси X
    Lx = X[:mid]
    Rx = X[mid:]

    Ly = []
    Ry = []
    for point in Y:
        if point.x < median:
            Ly.append(point)
        else:
            Ry.append(point)
    min_left = closest_dist(Lx, Ly)
    min_right = closest_dist(Rx, Ry)
    min_dist_over_halves = min(min_left, min_right)
    return closest_split_dist(X, Y, median, min_dist_over_halves)


def get_min_dist(points):
    X = sorted(points, key=lambda x: x[0])
    Y = sorted(points, key=lambda x: x[1])
    return closest_dist(X, Y)


if __name__ == '__main__':
    n = int(input())
    points = [Point(*map(int, input().split())) for _ in range(n)]
    print(f'{get_min_dist(points)}')
