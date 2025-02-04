def insertion_sort(unsorted: list):
    """
    # Insertion Sorting Algorithm

    Bubble sorting technique compares and swaps value one by one by traversing
    Insertion Sort is the sorting algorithm, that virtually creates sub-arrays
    of sorted and unsorted elements. Values from unsorted part are picked and
    inserted at the correct position of the sorted element.

    Initially, first 2 elements of an array are compared and sorted if needed.
    after that, second item is compared with the third element and sorted if
    necessary (which may need sorting again within the sorted sub-array again)

    ##  For example:

    * `[ 4 2 9 0 7 5 1]`

    * [4 2] [9 0 7 5 1]    <- Sort 4 and 2 and add it to the sub array
    *  ^ ^
    * [2 4] [9 0 7 5 1]
    *    ^   ^
    * [2 4 9] [0 7 5 1]    <- Compare 4 and 9 as they do not need swapping, keep at is it
    *      ^   ^
    * [2 4 0 9] [7 5 1]    <- Compare and sort 9 and 0 (the sorted  sub-array again needs sorting)
    * [2 0 4 9] [7 5 1]    <- Compare and sort 4 and 0 (the sorted  sub-array again needs sorting)
    * [0 2 4 9] [7 5 1]    <- Compare and sort 2 and 0 (the sorted  sub-array again needs sorting)
    * ...
    insert and sort until all items in an array is sorted
    """
    # start from second index since we need at least 2 items in a sub-array ex: [0, 1]
    for index in range(1, unsorted.__len__()):
        # 1 new item is added at last to the sorted sub-array to check it so, we
        # start checking it from reverse.
        # if it is not sorted, we swap item with the previous index
        for pointer in range(index, 0, -1):
            if unsorted[pointer] > unsorted[pointer - 1]:
                break
            unsorted[pointer], unsorted[pointer - 1] = (
                unsorted[pointer - 1],
                unsorted[pointer],
            )


if __name__ == "__main__":
    my_list = [4, 2, 9, 0, 7, 5, 1]
    print(f"Unsorted: {my_list}")
    insertion_sort(my_list)
    print(f"Sorted: {my_list}")
