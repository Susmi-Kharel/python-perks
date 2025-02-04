def selection_sort(unsorted: list):
    """
    # Selection Sort

    Selection sort is another sorting algorithm, which compares smallest of all
    values and and put it in the first position. Similarly, after swapping value,
    it will find out second most smallest value and swap it  with second item in
    the array.

    Unlike bubble sort, the sorting will be done from the beginning.

    ## Example:

    - 4 2 9 0 7 5 1   <- Swap 4 and 0
    - ^     ^
    - [0] 2 9 4 7 5 1 <- 0 is sorted
    - [0] 2 9 4 7 5 1 <- Swap 2 and 1
    -     ^         ^
    -...
    Swap values until all values are sorted
    """

    """
        for i in 0..array.len() {
        let mut smallest = i;
        for j in i..array.len() {
            if array[smallest] > array[j] {
                smallest = j;
            }
        }
        if smallest != i {
            print!(
                "Swapping {} and {} from {:?} -> ",
                array[smallest], array[i], array
            );
            array.swap(i, smallest);
            println!("{:?}", array)
        }
    }
    """
    for index in range(0, unsorted.__len__()):
        smallest = index
        for target in range(index, unsorted.__len__()):
            if unsorted[smallest] > unsorted[target]:
                smallest = target
        if smallest != index:
            unsorted[index], unsorted[smallest] = (
                unsorted[smallest],
                unsorted[index],
            )


if __name__ == "__main__":
    my_list = [4, 2, 9, 0, 7, 5, 1]
    print(f"Unsorted: {my_list}")
    selection_sort(my_list)
    print(f"Sorted: {my_list}")
