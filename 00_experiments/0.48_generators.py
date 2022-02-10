# gen1.py
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        yield f'This is the {num} yield statement.'


def finite_sequence():
    nums = [1, 2, 3]
    for num in nums:
        yield num


# nums_squared_lc = [num ** 2 for num in range(5)]
# nums_squared_gc = (num ** 2 for num in range(5))

if __name__ == '__main__':
    # infinite = infinite_sequence()
    finite = finite_sequence()
    for n in finite:
        print(n, end=' ')

