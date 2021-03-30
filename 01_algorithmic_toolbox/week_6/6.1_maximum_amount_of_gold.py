def knapsack_without_repetitions(W, weights):
    # F[w, j] is max cost of filling a knapsack with a maximum weight of 'w' kg using only first i elements
    F = [[None for j in range(n + 1)] for w in range(W + 1)]

    # F[w][0] is max cost when filling in the knapsack of different max weights w = 0...W with 0 allowed elements
    for w in range(W + 1):
        F[w][0] = 0

    # F[0][j] is max cost when filling in the knapsack of weight = 0 with 0...n allowed elements
    for j in range(n + 1):
        F[0][j] = 0

    for w in range(1, W + 1):
        for j, curr_w in enumerate(weights, start=1):
            if w - curr_w >= 0:
                F[w][j] = max(F[w-curr_w][j-1] + curr_w,
                              F[w][j-1])
            else:
                F[w][j] = F[w][j-1]

    return F


if __name__ == '__main__':
    W, n = map(int, input().split())
    weights = [int(x) for x in input().split()]

    dp_table = knapsack_without_repetitions(W, weights)

    print(dp_table[-1][-1])
