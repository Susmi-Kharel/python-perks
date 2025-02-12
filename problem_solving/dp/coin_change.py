"""
Coin Change Problem
-------------------

A coin change problem requires us to find out the minimum number of coins from
the given set of coins to change the given amount considering that any number of
coins can be used from the given coin options.

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
