def bubble_sort(unsorted: list):
    """
    # Bubble Sorting Algorithm

    Bubble sorting technique compares and swaps value one by one by traversing
    through the list.

    If there are no swaps, the sorting is complete.

    ## example:

    ### step 1
    - (4  2) 9  0  7  5  1     <- Swap 4 and 2
    -  2 (4  9) 0  7  5  1
    -  2  4 (9  0) 7  5  1     <- Swap 9 and 0
    -  2  4  0 (9  7) 5  1     <- Swap 9 and 7
    -  2  4  0  7 (9  5) 1     <- Swap 9 and 5
    -  2  4  0  7  5 (9  1)     <- Swap 9 and 1
    -  2  4  0  7  5  1 [9]     <- [9] is sorted

    ### Step 2 : 9 is sorted so sort remaining

    - (2  4) 0  7  5  1 [9]
    -  2 (4  0) 7  5  1 [9]   <- sort 4 and 0
    - ...
    -  2  0  4  5  1 [7  9]     <- [7, 9] are sorted

    *  do this process until every elements are sorted
    """
    for i in range(0, unsorted.__len__()):
        swapped = False
        for j in range(0, unsorted.__len__() - i - 1):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                swapped = True
        # If no items swapped in the internal loop, then all items are sorted
        # and there is no longer need to continue the loop.
        if not swapped:
            break


if __name__ == "__main__":
    my_list = [4, 2, 9, 0, 7, 5, 1]
    print(f"Unsorted: {my_list}")
    bubble_sort(my_list)
    print(f"Sorted: {my_list}")
