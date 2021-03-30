def knapsack_with_repetitions(W, weights, c):
    F = [0 for _ in range(W+1)]
    for i in range(1, W+1):              # F[i] is max cost of filling a knapsack with a maximum weight of i kg
        for j, w in enumerate(weights):  # w is current weight from item weights array
            if w <= i:
                F[i] = max(F[i], F[i-w] + c[j])
    return F


if __name__ == '__main__':
    W, n = map(int, input().split())
    weights = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    dp_table = knapsack_with_repetitions(W, weights, c)

    print(dp_table[-1])



