# Instead of filling in only one knapsack (as in classical variant of the problem),
# we fill two knapsacks each with capacity sum/3, and try to maximize the weight in it.
# So by maximizing weight of each of 2 knapsacks I meant that I'm aiming to fill in the knapsacks
# in such a way that there is no empty space in each, so their maximum combined weight will be 2*sum/3
# where sum = (sum(numbers) // 3) if sum(numbers) is divisible by 3


# TO DO: разобраться с индексами
# slightly modified solution for classical knapsack without repetitions problem
# so by W we meant max sum = S//3, and by weights - natural numbers 1...n
def fill_in_left_surface(F, W, weights):
    # F[i][j][0] is max weight of filling in FIRST knapsack of capacity 'i' kg using only first j elements

    # F[i][0][0] - knapsack capacity is 0
    for i in range(W + 1):
        F[i][0][0] = 0

    # F[0][j][0] is max weight if there no allowed elements
    for j in range(W + 1):
        F[0][j][0] = 0

    for i in range(1, W + 1):
        for j, curr_w in enumerate(weights, start=1):
            if i - curr_w >= 0:
                F[i][j][0] = max(F[i - curr_w][j - 1][0] + curr_w,
                                 F[i][j - 1][0])
            else:
                F[i][j][0] = F[i][j - 1][0]
    print(F)


def can_partition_in_3_subsets(nums):
    S = sum(nums) // 3
    n = len(nums)

    # F[i][j][k] represents the maximum combined weight of two knapsacks of capacity 'j' and 'k' respectively
    F = [[[None for k in range(S + 1)] for j in range(S + 1)] for i in range(len(nums) + 1)]

    # F[0][j][k] means there are no items available to pick from, so without any item we can compose only weight = 0
    # F[0][j][k] = 0 means that front surface of the 3x3 matrix would be filled in with zeroes
    for j in range(S + 1):
        for k in range(S + 1):
            F[0][j][k] = 0

    # F[i][j][0] and F[i][0][k] corresponds to the left and bottom surfaces of the 3x3 matrix
    # and represent classical knapsack problem without repetitions so in order to fill in left and top surfaces
    # of the 3x3 matrix we should solve these cases using regular DP knapsack approach
    fill_in_left_surface(F, S, nums)

    return F


if __name__ == '__main__':
    n = int(input())
    nums = [int(x) for x in input().split()]

    if sum(nums) % 3 != 0:  # impossible to split all numbers into three parts
        print(0)
    else:
        dp_table = can_partition_in_3_subsets(nums)
