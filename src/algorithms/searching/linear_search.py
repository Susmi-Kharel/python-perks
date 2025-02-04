def linear_search(data, item) -> int | None:
    """# Linear Search

    Linear searching algorithm is a sequential searching algorithm, where we
    traverse through each item by index and compare every element to the desired
    element and return the index of the element.

    For a linear search, we do not need the list/array to be sorted since we
    check each item one by one.

    The Time complexity of the linear search is O(n)

    ## Example:

    Given array: [1, 5, 9, 2, 4], we want to search 9.
    - step 1: check first item (index = 0), item = 1 , != 9
    - step 2: check second item (index = 1), item = 5 , != 9
    - step 3: check third item (index = 2), item = 9 , == 9 [return index : 2]
    """
    for index, _item in enumerate(data):
        if _item == item:
            return index
    return None


if __name__ == "__main__":
    data = [1, 4, 7, 8, 9, 10, 11, 12, 15, 20]
    print(f"list: {data}")
    item = int(input("Enter item to search: "))
    if index := linear_search(data, item):
        print(f'The item "{item}" is at index {index}')
    else:
        print(f'The item "{item}" does not exist in the list')
