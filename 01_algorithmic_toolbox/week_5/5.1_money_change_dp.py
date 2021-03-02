# Good job! (Max time used: 0.01/5.00, max memory used: 9125888/536870912.)
def money_change_dp(money, coins):
    # base cases
    # min number of coins to make change for 0 cents = 0: F[0] = 0
    # min number of coins to make change for 1 cents = 0: F[1] = 1
    if money <= 1:
        return money
    F = [0, 1]

    for val in range(2, money+1):
        F.append(1 + min([F[val-coin] for coin in coins if val-coin >= 0]))
    return F[-1]


if __name__ == '__main__':
    coins = [1, 3, 4]
    money = int(input())
    min_number_of_coins = money_change_dp(money, coins)
    print(min_number_of_coins)

