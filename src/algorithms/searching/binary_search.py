from typing import TypeVar


def binary_search(sorted_list: list, item: int) -> int | None:
    """# Binary Search
    Binary Searching algorithm uses divide and conquer method to recursively find
    out elements of the item.

    It first compares middle most item of an array and recursively divides the
    array into sub-arrays virtually until it finds out the exact element.

    It works recursively and non-recursively, but as recursive functions are not
    good for larger arrays, we implemented while loop.

    The Time complexity of a binary search is O(log(n))

    ## NOTE:
    The binary search works only on the sorted array. If an array is not sorted,
    we must sort it before we implement this algorithm.

    We can use python's sort() method to sort the list before feeding it to this
    function for now.
    If you want to learn more about sorting algorithm, you can check
    `src/algorithms/sorting/`.

    ## Example,

    we have an array [1, 3, 4, 6, 7, 8, 9] and we want to find out an index of 7

    - step 1: compare the middle most item with 7 [6 < 7]
    - step 2: split an array and take the right slice [7 8 9] (take left if the comparison was different)
    - step 3: compare the middle most item of [7 8 9], i.e [8 > 7] (take the left slice)
    - step 4: compare the middle most item fo [7]: i.e [7 == 7]; return index of that number
    """
    #
    left = 0
    right = sorted_list.__len__() - 1

    while left < right:
        mid = (left + right) // 2
        mid_item = sorted_list[mid]
        print(f"index: {mid}, item:{sorted_list[mid]}")
        if mid_item == item:
            return mid
        elif mid_item < item:
            left = mid + 1
        else:
            right = mid - 1
    return None


if __name__ == "__main__":
    sorted_list = [1, 4, 7, 8, 9, 10, 11, 12, 15, 20]
    print(f"list: {sorted_list}")
    item = int(input("Enter item to search: "))
    if index := binary_search(sorted_list, item):
        print(f'The item "{item}" is at index {index}')
    else:
        print(f'The item "{item}" does not exist in the list')
