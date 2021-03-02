from copy import deepcopy
from math import inf


# TO DO: разобраться, как работает этот алгоритм Певзнера и сравнить его по времени работы с моим
def recursive_change_pevzner(money, coins):
    if money == 0:
        return 0
    minNumCoins = inf
    for i in range(len(coins)):
        if money >= coins[i]:
            numCoins = recursive_change_pevzner(money - coins[i], coins)
            if numCoins + 1 < minNumCoins:
                minNumCoins = numCoins + 1
    return minNumCoins


def get_MINIMUM_number_of_ways_to_make_change(denominations, change, count=0, idx=0):
    if change < 0:
        return 0
    if idx >= len(denominations):
        return 0
    if change == 0:
        return count

    incl = get_MINIMUM_number_of_ways_to_make_change(denominations, change - denominations[idx], count + 1, idx)
    excl = get_MINIMUM_number_of_ways_to_make_change(denominations, change, count, idx + 1)

    if bool(incl) ^ bool(excl):  # using truth table for XOR
        return incl if incl else excl
    else:
        return min(incl, excl) if (incl and excl) else 0


def get_total_number_of_ways_to_make_change(denominations, change, idx=0):
    if change < 0:
        return 0
    if idx >= len(denominations):
        return 0
    if change == 0:
        return 1

    incl = get_total_number_of_ways_to_make_change(denominations, change - denominations[idx], idx)
    excl = get_total_number_of_ways_to_make_change(denominations, change, idx + 1)

    return incl + excl


def print_readable(raw_data, denominations, change):
    len_input_lst = len(raw_data)
    len_output_lst = len(denominations)
    combinations = [raw_data[i:i + len_output_lst] for i in range(0, len_input_lst, len_output_lst)]
    zipped_combs = [list(zip(denominations, lst)) for lst in combinations]

    print(
        f'There are possible to make change of value = {change} in {len(combinations)} ways using {denominations} denominations.')
    print(f'Possible combinations:')

    s = []
    for i, comb in enumerate(zipped_combs):
        for tpl in comb:
            if tpl[1]:
                s.append(f'[{tpl[0]} cent] x {tpl[1]}')
        print(f'{i + 1}) ' + ' + '.join(s))
        s = []


# d - list of integers representing available coin denominations
# idx - index of current denomination in list d
def make_change_recursive(d, change, used_coins, idx=0):
    # ############### Base cases ###############
    # 1) solution found
    if change == 0:
        return used_coins

    # 2) change became negative, return None
    if change < 0:
        return None

    # 3) all possible denominations are used, there are no denominations left in array (list) d
    if idx >= len(d):
        return None
    # ############ End of base cases ############

    # Case 1. Include current denomination `d[idx]` in solution and recur with remaining
    # 'change = change - d[idx]' with the same number of denominations (idx won't be changed) to use
    tmp_lst = [x if i != idx else x + 1 for i, x in enumerate(used_coins)]
    incl = make_change_recursive(d, change - d[idx], deepcopy(tmp_lst), idx)

    # Case 2. Exclude current denomination `d[idx]` from consideration and recur
    # for remaining 'len(d) - (idx + 1)' denominations
    excl = make_change_recursive(d, change, deepcopy(used_coins), idx + 1)

    if bool(incl) ^ bool(excl):
        return incl if incl else excl
    else:
        return incl + excl if (incl and excl) else None


if __name__ == '__main__':
    denominations = [2, 3, 5]
    change = 7

    # denominations = [50, 30, 20, 1]
    # change = 90

    # denominations = [2, 4, 8]
    # change = 997

    # raw_data = make_change_recursive(denominations, change, [0] * len(denominations))
    # print_readable(raw_data, denominations, change)

    # number_of_ways = get_total_number_of_ways_to_make_change(denominations, change)
    # print(f'There are {number_of_ways} number of ways to make change to {change} using denominations: {denominations}')

    # min_number_of_coins = get_MINIMUM_number_of_ways_to_make_change(denominations, change)
    # print(f'Minimun number of coins to make change to {change} using {denominations}: {min_number_of_coins}')

    min_number_of_coins = recursive_change_pevzner(change, denominations)
    print(f'min_number_of_coins = {min_number_of_coins}')
