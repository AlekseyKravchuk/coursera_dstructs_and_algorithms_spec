from math import inf


def restore_numbers(F):
    i = len(F) - 1
    lst = [i]
    while i != 1:
        if F[i][1] == 0:
            lst.append(i//3)
            i = i // 3
        elif F[i][1] == 1:
            lst.append(i//2)
            i = i // 2
        elif F[i][1] == 2:
            lst.append(i-1)
            i = i - 1
    return lst[::-1]


def get_arguments(n):
    args = []
    args.append(n // 3) if n % 3 == 0 else args.append(0)
    args.append(n // 2) if n % 2 == 0 else args.append(0)
    args.append(n - 1)

    # return list of outcomes when operation = {n/3, n/2, n-1} being applied
    # if operation is not applicable, adds 0 to corresponding place in the list
    return args


def min_number_of_operations(n):
    F = [(inf, -1), (0, -1)]
    for i in range(2, n + 1):
        F_vals = [F[arg][0] for arg in get_arguments(i)]
        F_min = min(F_vals)
        F.append((1 + F_min, F_vals.index(F_min)))
    return F[-1][0], restore_numbers(F)


if __name__ == '__main__':
    n = int(input())
    minval, numbers = min_number_of_operations(n)
    print(minval)
    for elm in numbers:
        print(elm, end=' ')
    print()

