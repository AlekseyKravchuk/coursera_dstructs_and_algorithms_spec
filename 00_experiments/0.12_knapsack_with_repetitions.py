# test input
"""
10 4
6 3 4 2
30 14 16 9
"""


def knapsack_with_repetitions(W, weights, c):
    F = [0 for _ in range(W+1)]
    for w in range(1, W+1):  # F[w] is max cost of filling a knapsack of max w = w kg
        for j, _ in enumerate(weights):  # curr_weight is current weight from item weights array
            if weights[j] <= w:
                F[w] = max(F[w], F[w-weights[j]] + c[j])
    return F


if __name__ == '__main__':
    W, n = map(int, input().split())
    weights = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    dp_table = knapsack_with_repetitions(W, weights, c)

    print(dp_table[-1])



