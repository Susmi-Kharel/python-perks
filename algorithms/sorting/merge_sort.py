def merge(left: list, right: list):
    merged = []

    while True:
        left_exhausted = not left.__len__()
        right_exhausted = not right.__len__()
        # print("⛔ left: ", left, "right: ", right, "Merged: ", merged)

        if left_exhausted and right_exhausted:
            break

        if left_exhausted:
            merged.append(right.pop(0))

        elif right_exhausted:
            merged.append(left.pop(0))

        elif left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    return merged


def merge_sort(data: list):
    """
    # Merge Sort
    ------------

    Merge sort is an efficient sorting algorithm, which works in a divide and
    conquer method. It first splits the sub-array until single element is left
    in each split, after that, it starts  merging all one by one.

    Example:
    We have an array [ 7, 3 10, 2], we start splitting it in the middle until
    we get single element in an array

    * STEP 1(split):              [ 7, 3] [10, 2]
    * STEP 2(further split):      [7] [3] [10] [2]
    we have single element, so we start merging arrays by sorting it
    At this point, we compare each element and select smallest to put at index 0
    for this we start comparing each item at index 0 since it is the smallest in
    each array.
    after that, we put another element by comparing

    * STEP 3(merge singles):      [3, 7] [2, 10]
    ... repeat until the whole array is sorted
    * STEP 4(merge doubles):      [2, 3, 7, 10]
    ...

    * Time complexity of Merge sort is O(n log(n) )

    *Tradeoffs:
    - It has more space complexity since it requires storage to store temporary
      results
    - It requires copying sub arrays from the original array since we can not
      directly swap elements in place.
    """

    if data.__len__() <= 1:
        return data

    mid_ptr = data.__len__() // 2
    # split and merge
    left, right = data[:mid_ptr], data[mid_ptr:]
    return merge(merge_sort(left), merge_sort(right))


if __name__ == "__main__":
    unsorted = [4, 2, 9, 0, 7, 5, 1]
    sorted = merge_sort(unsorted)
    print("Unsorted Data: ", unsorted)
    print("Sorted Data: ", sorted)
