"""
# Median
--------

Median is a statistical calculation procedure that finds out the number that
separates the higher half of the numbers from a list with lower half.

Generally, when we have odd number of elements, we have the number in the list,
however, if there are even number of elements, we have to find the mean of two
median values.

if x(n) is nth element of the list, then

         |  x((n+1)/2)                  if n is odd
median = |
         |  (x(n/2) + x((n/2)+1)/2     if n is even

NOTE: The index starts at 0 in python so while of finding out nth element, we
      have to find out element at (n-1)th index hence,
      x((n+1)/2) becomes x((n+1)/2 -1) and
      x((n/2) becomes x((n/2 -1))
"""


def median(items: list[int]):
    """
    Median needs sorted list since we will find out the middle number that is in
    ascending order.
    """
    items.sort()
    n = items.__len__()

    if n % 2 == 1:
        return items[(n + 1) // 2 - 1]
    else:
        return (items[n // 2 - 1] + items[n // 2]) / 2


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    print(f"Median of the list is : {median(list)}")  # 3

    list = [1, 2, 3, 4, 5, 6]
    print(f"Median of the list is : {median(list)}")  # 3.5
