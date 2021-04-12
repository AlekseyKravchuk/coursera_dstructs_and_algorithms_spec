def restore_solution(dp_2x2, W, items):
    solution = []
    i = len(dp_2x2) - 1
    cap = len(dp_2x2[0]) - 1
    while dp_2x2[i][cap] != 0:
        if cap - items[i-1] >= 0:
            if dp_2x2[i][cap] == dp_2x2[i-1][cap - items[i-1]] + items[i-1]:
                solution.append(items[i-1])
                cap -= items[i-1]
        i -= 1

    return solution


def knapsack_without_repetitions(W, weights):
    # F[i][cap] is max cost of filling a knapsack of capacity 'cap' kg using only first i elements
    F = [[None for j in range(W + 1)] for w in range(n + 1)]

    # F[0][cap] is max weight when filling in the knapsack of different capacities cap = 0...W with NO allowed elements
    # fill in first ROW in 2x2 DP table with zeroes
    for cap in range(W + 1):
        F[0][cap] = 0

    # F[i][0] is max cost when filling in the knapsack of weight = 0 with 0...n allowed elements
    # fill in first COLUMN in 2x2 DP table with zeroes
    for i in range(n + 1):
        F[i][0] = 0

    for i, curr in enumerate(weights, start=1):
        for cap in range(1, W + 1):
            if cap - curr >= 0:
                F[i][cap] = max(F[i - 1][cap - curr] + curr,
                                F[i - 1][cap])
            else:
                F[i][cap] = F[i - 1][cap]

    return F


if __name__ == '__main__':
    W, n = map(int, input().split())
    weights = [int(x) for x in input().split()]
    weights.sort()
    dp_table = knapsack_without_repetitions(W, weights)
    print(dp_table[-1][-1])
    solution = restore_solution(dp_table, W, weights)
    print(solution)
