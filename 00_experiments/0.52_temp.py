def f_der_val(x):
    # return 3 * x ** 2 - 1
    # return 2 * x
    # return 4 * x**3
    return 3 * x ** 2 - 9

def get_new_location(x):
    step = 0.1
    return x - step*f_der_val(x)


def print_locations(x=-2, n_iterations=3):
    for _ in range(n_iterations):
        print(f'\tx = {x:.3f}, f_der(x) = {f_der_val(x):.3f}')
        x = get_new_location(x)



if __name__ == '__main__':
    # print(f'Type in current location, x: ')
    # x = int(input())
    # n = 10
    # print(f'New location: {get_new_location(x)}')
    print(f'Locations:')
    # print_locations(x, n)
    # print_locations(0, 50)
    print_locations()