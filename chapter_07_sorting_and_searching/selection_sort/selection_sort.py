def selection_sort(unsorted_list: list[int]) -> list[int]:
    # copy the input for preventing the mutation of input
    copied_input = [i for i in unsorted_list]
    length = len(copied_input)

    # outer loop:
    # - iterate elements from 0 to just before of last-most
    # - regard this zone as ordered zone
    for i in range(length - 1):
        # set the i (index) as the ordered zone's last element
        idx_of_min = i
        # inner loop:
        # - iterate elements from i to last-most
        # - regard this zone as unordered zone
        for j in range(i, length):
            # renew the minimum value's index with loop
            if copied_input[j] < copied_input[idx_of_min]:
                idx_of_min = j
        # swap the minimum value's index and ordered zone's last element's index
        copied_input[i], copied_input[idx_of_min] = copied_input[idx_of_min], copied_input[i]

    # return the sorted list
    return copied_input
