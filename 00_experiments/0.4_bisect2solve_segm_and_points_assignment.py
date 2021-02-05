import bisect

if __name__ == '__main__':
    # x = ['apple', 'banana', 'banana', 'banana', 'banana', 'banana', 'orange', 'pineapple']
    # elm2search = 'banana'
    total_num_of_segments = 4
    points = [7, 3, 5]
    counts = [total_num_of_segments] * len(points)
    x = [2, 3, 5, 5, 5, 5, 7, 9, 11]
    elm2search = 3
    to_the_left_of_curr_point = bisect.bisect_left(x, elm2search)
    to_the_right_of_curr_point = len(x) - bisect.bisect_right(x, elm2search)
    print(f'to_the_left_of_curr_point = {to_the_left_of_curr_point}')
    print(f'to_the_right_of_curr_point = {to_the_right_of_curr_point}')
    print(f'counts = {counts}')