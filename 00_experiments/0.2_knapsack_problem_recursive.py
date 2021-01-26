WEIGHT_LIMIT = 5
value = [3, 9, 12, 8]
weight = [1, 3, 4, 2]


# pos - index the current item , selected - list of indices
def knapsack(pos, selected):
    totalValue = 0
    totalWeight = 0

    for i in selected:
        totalValue += value[i]
        totalWeight += weight[i]

    # Base case: WEIGHT_LIMIT is exceeded
    if totalWeight > WEIGHT_LIMIT:
        return (0, 0)

    # Base case: No items left to choose
    if pos >= len(weight):
        return (totalValue, totalWeight)


    # Recursive case
    ans1 = knapsack(pos + 1, selected + [pos])  # Switch ON
    ans2 = knapsack(pos + 1, selected.copy())  # Switch OFF

    if ans1[0] > ans2[0]:
        return ans1
    else:
        return ans2


ans = knapsack(0, [])
print(ans)
