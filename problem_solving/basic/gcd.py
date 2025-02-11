"""
Greatest Common Divisor (GCD)
-----------------------------

Greatest Common Divisor or the highest common factor is a common divisor of the
given numbers.

It is the largest positive integer that divides both numbers without leaving
remainders.

For example numbers 12 and 18 has GCD 6

"""

from functools import reduce


def _gcd(a: int, b: int):
    """
    Finding out GCD between 2 numbers is so easy in python. we try to perform
    modulo operator between 2 numbers until we find remainder to be 0.

    For example we have 2 numbers 48 and 64

    a = 48, b = 64
    Step 1: (a, b) = (b, a%b) = (64, 48 % 64) = (64, 48)    b != 0
    Step 2: (a, b) = (48, 64 % 48) = (48, 16)               b != 0
    Step 3: (a, b) = (16, 48 % 16) = (16, 0)                b == 0

    Setp 4: b == 0, so GCD = a = 16

    """
    # find out gcd between 2 numbers
    while b:
        a, b = b, a % b
    return a


def gcd(numbers: list[int]) -> int:
    """
    To find out gcd between multiple numbers, we simply reduce the above _gcd
    function to each numbers in the list.

    """
    return reduce(_gcd, numbers)


if __name__ == "__main__":
    print(_gcd(1, 2))  # 1
    print(_gcd(12, 18))  # 6
    print(_gcd(9, 18))  # 9
    print(_gcd(32, 40))  # 8

    print(gcd([1, 2]))  # 1
    print(gcd([32, 40, 80]))  # 8
    print(gcd([32, 64, 96]))  # 32
    print(gcd([64, 96, 160, 320]))  # 32
    print(gcd([64, 96, 160, 320, 48]))  # 16
