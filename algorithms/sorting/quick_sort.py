def quick_sort(unsorted: list):
    """
    `Quick sort` is an efficient algorithm that follows divide-and-conquer
    approach

    Quick sorting process consists of the following steps:

    1. Pivot selection   : Choose pivot point/element from the array
    2. Partitioning      : Rearrange the array
    3. Recursion         : Split and select pivot point until sub-array contains single element
    4. Combination       : Rearrange and combine all single items
    """
    if len(unsorted) <= 1:
        return unsorted  # Base case: already sorted

    # Choose the middle element as a pivot element
    pivot = unsorted[len(unsorted) // 2]

    # partitioning
    left, middle, right = [], [], []

    for element in unsorted:
        if element < pivot:
            # add all elements to the left that are smaller than pivot
            left.append(element)
        elif element > pivot:
            # add all elements to the right that are greater than pivot
            right.append(element)
        else:
            # if element is same as pivot element, add it to the middle
            middle.append(pivot)

    # recursively perform sorting and merge all left to right partitions
    return [*quick_sort(left), *middle, *quick_sort(right)]


if __name__ == "__main__":
    my_list = [4, 2, 9, 0, 7, 5, 1]
    print(f"Unsorted: {my_list}")
    sorted = quick_sort(my_list)
    print(f"Sorted: {sorted}")
