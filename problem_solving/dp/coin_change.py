"""
Coin Change Problem
-------------------

A coin change problem requires us to find out the minimum number of coins from
the given set of coins to change the given amount considering that any number of
coins can be used from the given coin options.

The function should return the minimum number of coins that can be used to
change the given sum. If there are no changes, the function should return -1.

Example we have coins: 1, 2, 5 and we have to change coins with amount 11.
We may have different options:

1. 1 X 11 coins                 = 11 coins
2. 2 X 5 coins + 1 X 1 coins    = 6 coins
3. 5 X 2 coins + 1 X 1 coins    = 3 coins
4  1 X 6 coins + 5 X 1 coins    = 7 coins
....
and so on

but the change with option 3 will have minimum number of coins to change. so the
solution will be `3`.

"""

import sys


def coin_change(coins: list[int], sum: int) -> int:
    if sum == 0:
        return 0
    if coins.__len__() == 0:
        return -1

    # initialize a list that stores max number of coins used to change the given
    # number from amount 1 to the given sum.
    table = [sys.maxsize for _ in range(sum + 1)]

    # we always need 0 number of coins to change the sum 0 from a given options
    table[0] = 0

    # iterate from 1 upto the sum to find number of changes for each amount
    # we call it an intermediate sum, which will later be used to find the sum
    # for the next number
    for intermediate_sum in range(1, sum + 1):
        # iterate on each coins to find number of changes required
        for coin in coins:  # example: [1, 2, 5]
            # if the intermediate sum is less than the coin, discard it
            # since it cannot be changed with that coin
            if intermediate_sum >= coin:
                # We find the number of coins to change the amount `num` by
                # adding 1 to the previous change that was `num - coin`.
                # example: if we were about to change $50, and we already know that
                # we have 5 changes for $45 and we have $5 coin for change, we do not need to
                # find it from the start.
                coins_for_prev_change = table[intermediate_sum - coin]

                # check if the sub result is smallest when iterated over all the
                # available coins.
                # example: if sub_result when using coin 8 is smaller than using the coin 5,
                # we should choose the sub-result with coin 8 since it will give us smallest
                # number of coins to change the specified amount.
                if (
                    coins_for_prev_change != sys.maxsize
                    and coins_for_prev_change + 1 < table[intermediate_sum]
                ):
                    table[intermediate_sum] = coins_for_prev_change + 1
    # print(table)
    if table[sum] == sys.maxsize:
        return -1

    return table[sum]


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))  # 3  -> 5,5,1
    print(coin_change([1, 2, 5, 10], 49))  # 7 -> 10X4,5,2,2
    print(coin_change([1, 2, 5, 10], 88))  # 11 -> 10X8,5,2,1
