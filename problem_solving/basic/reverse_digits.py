"""
Reverse Digits of an integer
----------------------------

Given an integer, reverse all the digits of an integer mathematically. Example,
if an integer 12345 is given, the reversed integer should be 54321.

Mathematically reversing an integer requires a loop that divides the integer and
find outs the remainder to know the digit of one place and multiplying back by
10 and adding the remainder of the previous iteration until the number becomes 0.

Steps:
1. result = 0

2. divide the integer by 10 and find out remainder and result
    - number = num // 10    ->  12345 // 10 = 1234
    - r = num % 10          ->  12345 %10 = 5
    - num = number          -> 1234
3. now multiply the previous remainder by 10 and add with the current remainder
    - result = result * 10 + r
4. Repeat steps 2 and 3 until number becomes 0
"""


def reverse_digits(number: int) -> int:
    result = 0
    if number < 0:
        raise ValueError("Negative numbers not allowed")
    if number < 10:
        return number
    while number > 0:
        number, result = (number // 10, result * 10 + number % 10)
    return result


if __name__ == "__main__":
    print(reverse_digits(123))  # 321
    print(reverse_digits(12345))  # 54321
    print(reverse_digits(87214))  # 41278
