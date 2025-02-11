"""
# Practical Number Solution
---------------------------

A practical number is a positive integer where every smaller can be expressed as
a sum of distinct divisors of that number.

In other words, a number is a practical number whose divisors can be combined to
create a number below it.

For example 12 is a practical number.
It's divisors are: 1, 2, 3, 4, and 6.

1 -> 1
2 -> 2
3 -> 3
4 -> 4
5 -> 4 + 1
6 -> 6
7 -> 7 + 1
8 -> 6 + 2
9 -> 6 + 3
10 -> 6 + 4
11 -> 6 + 4 + 1

"""

import math


def find_divisors(num: int) -> list[int]:
    divisors = {1}
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            divisors.add(n)
            divisors.add(num // n)
    return list(divisors)


def has_sum(target: int, _set: list[int]):
    # if the number itself exists, or number return True
    if target == 0 or target in _set:
        return True

    sums = {0}

    for num in _set:
        new_sums = {x + num for x in sums}
        sums.update(new_sums)
        if target in sums:
            return True
    return False


def is_practical_number(num: int) -> bool:
    if num < 1:
        return False
    divisors = find_divisors(num)
    sum_previous = 1

    for i in range(1, len(divisors)):
        if divisors[i] > sum_previous + 1:
            return False
        sum_previous += divisors[i]

    for n in range(1, num):
        if not has_sum(n, divisors):
            return False
    return True


if __name__ == "__main__":
    for number in [8, 10, 12, 15]:
        print(
            f"{number:5d}: {'✅' if is_practical_number(number) else '⛔ Not'} Practical"
        )
