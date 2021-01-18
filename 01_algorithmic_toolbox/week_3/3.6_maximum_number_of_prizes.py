import math
from decimal import Decimal


def solve_quadratic_eq_for_sum_of_arithm_progression(S):
    a = 1
    b = 1
    c = (-2) * S
    D = (b ** 2) - (4 * a * c)  # D - discriminant
    x1 = (-b + math.sqrt(D)) / float(2 * a)
    x2 = (-b - math.sqrt(D)) / float(2 * a)
    if x1 >= 0:
        return x1
    if x2 >= 0:
        return x2


def print_max_number_of_top_places(S, n):
    frac_part = Decimal(str(n)) % 1
    if frac_part == 0.0:
        n = int(n)
        print(n)
        for i in range(1, n + 1):
            print(i, end=' ')
    else:
        print(int(n))

        new_n = int(n) - 1
        S_prev = int((1 + new_n)*new_n / 2)
        last_term = S - S_prev
        for i in range(1, new_n+1):
            print(i, end=' ')
        print(last_term)


def main():
    S = int(input())
    n = solve_quadratic_eq_for_sum_of_arithm_progression(S)
    print_max_number_of_top_places(S, n)


if __name__ == '__main__':
    main()
