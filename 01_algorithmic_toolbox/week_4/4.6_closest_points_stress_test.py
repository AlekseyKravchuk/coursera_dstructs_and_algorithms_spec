from collections import namedtuple
from math import inf
from math import sqrt
import random

Point = namedtuple('Point', ['x', 'y'])

# #################################### ANOTHER SOLUTION ###################################
def dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)  # store length - quicker
    mx_x = p_x[ln_x // 2][0]  # select midpoint on x-sorted array

    # Create a subarray of points not further than delta from midpoint on x-sorted array
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]

    best = delta  # assign delta value to best
    ln_y = len(s_y)  # store length of subarray for quickness
    for i in range(ln_y - 1):
        for j in range(i + 1, min(i + 5, ln_y)):  # We have to check only next 5 points; proof found in literature
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best


def brute(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi
    for i in range(ln_ax - 1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1:
                d = dist(ax[i], ax[j])
                if d < mi:  # Update min_dist and points
                    mi = d
                    p1, p2 = ax[i], ax[j]
    return p1, p2, mi


def closest_pair(ax, ay):
    ln_ax = len(ax)  # It's quicker to assign variable
    if ln_ax <= 3:
        return brute(ax)  # A call to bruteforce comparison
    mid = ln_ax // 2  # Division without remainder, need int
    Lx = ax[:mid]  # Two-part split
    Rx = ax[mid:]

    midpoint = ax[mid][0]
    Ly = list()
    Ry = list()
    for x in ay:  # split ay into 2 arrays using midpoint
        if x[0] < midpoint:
            Ly.append(x)
        else:
            Ry.append(x)
    # Call recursively both arrays after split
    (p1, q1, mi1) = closest_pair(Lx, Ly)
    (p2, q2, mi2) = closest_pair(Rx, Ry)

    # Determine smaller distance between points of 2 arrays
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)

    # Call function to account for points on the boundary
    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)
    # Determine smallest distance for the array
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3


def solution(a):
    ax = sorted(a, key=lambda x: x[0])  # Presorting x-wise O(nlogn)
    ay = sorted(a, key=lambda x: (x[1], x[0]))  # Presorting y-wise then x-wise O(nlogn)
    p1, p2, mi = closest_pair(ax, ay)  # Recursive D&C function
    return mi
# ################################ END OF ANOTHER SOLUTION ################################

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ################################ MY SOLUTION ################################
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
    # strip = [point for point in Y if abs(point.x - median) < min_dist]
    # for i, curr_point in enumerate(strip):
    #     for j in range(i + 1, min(i + 6, len(strip))):
    #         if strip[j].y - curr_point.y < min_dist:
    #             dist = euclidean_dist(curr_point, strip[j])
    #             if dist < min_dist:
    #                 min_dist = dist
    #         else:
    #             break
    # return min_dist

    strip = [point for point in Y if abs(point.x - median) < min_dist]
    for i, curr_point in enumerate(strip):
        for j in range(i + 1, min(i + 6, len(strip))):
            dist = euclidean_dist(curr_point, strip[j])
            if dist < min_dist:
                min_dist = dist

    return min_dist


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
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ################################ END OF MY SOLUTION ################################

if __name__ == '__main__':
    # n = int(input())
    # points = [Point(*map(int, input().split())) for _ in range(n)]
    # print(f'{get_min_dist(points)}')
    num_of_points = 6
    start = -10
    end = 10

    while True:
        points_for_outer_func = [[random.randint(start, end), random.randint(start, end)] for i in range(num_of_points)]
        points_for_my_func = [Point(*point) for point in points_for_outer_func]
        # points_for_my_func = [Point(-8, 9), Point(-8, 3), Point(-4, 7), Point(-1, 1), Point(6, 6), Point(10, -8)]
        # points_for_outer_func = [[-8, 9], [-8, 3], [-4, 7], [-1, 1], [6, 6], [10, -8]]

        res_by_outer_func = solution(points_for_outer_func)
        res_by_my_func = get_min_dist(points_for_my_func)
        if res_by_outer_func == res_by_my_func:
            print('OK')
        else:
            print(f'Failed test case identified:')
            print('Input:')
            print('********************************')
            print(f'{len(points_for_my_func)}')
            for point in points_for_my_func:
                for coord in point:
                    print(coord, end=' ')
                print()
            print('********************************')
            print(f'res_by_outer_func = {res_by_outer_func}')
            print(f'res_by_my_func = {res_by_my_func}')
            break

