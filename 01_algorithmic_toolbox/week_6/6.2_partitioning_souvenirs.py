# Instead of filling in only one knapsack (as in classical variant of the problem),
# we fill in the two knapsacks each with capacity S/3, and try to maximize the common weight of
# both knapsacks. So by maximizing weight of each of 2 knapsacks I meant that I'm aiming to fill in the knapsacks
# in such a way that there is no empty space in each, so their maximum combined weight will be 2*S/3
# where S = (sum(numbers) // 3) if sum(numbers) is divisible by 3

# slightly modified solution for classical knapsack without repetitions problem
# so by W we meant max sum = S//3, and by weights - natural numbers 0...n
def fill_in_left_surface(F, S, nums):
    N = len(nums)
    # F[i][cap][0] is max weight of filling in FIRST knapsack of capacity cap=0...S kg using only first i=0...N elements

    # F[i][0][0] corresponds to case when knapsack capacity=0
    for i in range(N + 1):
        F[i][0][0] = 0

    # F[0][cap][0] is max weight if there no allowed elements
    for cap in range(S + 1):
        F[0][cap][0] = 0

    for i, num in enumerate(nums, start=1):
        for cap in range(S+1):
            if cap - num >= 0:
                F[i][cap][0] = max(F[i-1][cap - num][0] + num,
                                   F[i-1][cap][0])
            else:
                F[i][cap][0] = F[i-1][cap][0]
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

    # F[i][j][0] and F[i][0][k] correspond to the left and bottom surfaces of the 3x3 DP matrix respectively
    # and represent classical knapsack problem without repetitions so in order to fill in left and top surfaces
    # of the 3x3 matrix we should solve these cases using regular DP knapsack approach
    fill_in_left_surface(F, S, nums)

    # when filling in the top surface, the values will be the same as in left surface
    for i in range(n+1):
        for k in range(S+1):
            F[i][0][k] = F[i][j][0]

    # now we have filled in front, left and top surfaces of 3x3 DP matrix,
    # so we can fill in the rest cells of DP matrix:
    for i, num in enumerate(nums, start=1):
        for j in range(S+1):
            for k in range(S+1):
                if j - num >= 0 and k - num >= 0:
                    F[i][j][k] = max(F[i-1][j-num][k],
                                     F[i-1][j][k-num],
                                     F[i-1][j][k])
    return F


if __name__ == '__main__':
    n = int(input())
    nums = [int(x) for x in input().split()]

    if sum(nums) % 3 != 0:  # impossible to split all numbers into three parts
        print(0)
    else:
        dp_table = can_partition_in_3_subsets(nums)
        print(dp_table[-1][-1][-1])
