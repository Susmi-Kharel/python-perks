"""
Find the nth item of a fibonacci series
---------------------------------------

Fibonacci Series is a series in which a number in a series is equal to the sum
of last 2 numbers in the series.

An example of a fibonacci series is 1, 1, 2, 3, 5, 8, 13, 21, 34...

Nth item of fibonacci series can be solved both using dynamic programming and
recursion however recursive functions will be much slower for higher value of n
so it is recommended to use dynamic programming to find it out.
"""


def fibonacci_recursion(n: int) -> int:
    if n < 1:
        raise ValueError("Negative number is not acceptable")
    if n < 3:
        return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def fibonacci(n: int):
    if n < 1:
        raise ValueError("Negative number is not acceptable")
    if n < 3:
        return 1
    a, b = 1, 1
    for n in range(3, n + 1):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    print(fibonacci_recursion(8))  # 21
    print(fibonacci_recursion(9))  # 34
    print(fibonacci_recursion(10))  # 55
    # It takes too long to find out the number for higher value of N
    # and eventually maximum depth of recursion will be exceeded in such case
    # print(fibonacci_recursion(40))     # 102334155 (very slow)

    print(fibonacci(8))  # 21
    print(fibonacci(9))  # 34
    print(fibonacci(10))  # 55
    print(fibonacci(40))  # 102334155
    print(fibonacci(100))  # 354224848179261915075
