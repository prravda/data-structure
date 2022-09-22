# 3.5
def find_largest(l: list[int]) -> int:
    largest = 0
    for e in l:
        if e > largest:
            largest = e
    return largest


# 3.6
def find_largest_and_smallest(l: list[int]) -> tuple[int, int]:
    largest = 0
    smallest = 99999

    for e in l:
        if e > largest:
            largest = e
            continue
        if e < smallest:
            smallest = e
            continue

    return largest, smallest


# 3.7
def find_duplication(list_one: list[int], list_two: list[int]) -> bool:
    for i in list_one:
        for j in list_two:
            if i == j:
                return True
    return False


# Using brute-force, not sort() method
def merge_and_sort(ordered_list_one: list[int], ordered_list_two: list[int]) -> list[int]:
    merged_list = [None for i in range(len(ordered_list_one) + len(ordered_list_two))]

    i = 0
    j = 0
    k = 0

    while i < len(ordered_list_one) and j < len(ordered_list_two):
        if ordered_list_one[i] < ordered_list_two[j]:
            merged_list[k] = ordered_list_one[i]
            k += 1
            i += 1
        else:
            merged_list[k] = ordered_list_two[j]
            k += 1
            j += 1

    while i < len(ordered_list_one):
        merged_list[k] = ordered_list_one[i]
        k += 1
        i += 1

    while j < len(ordered_list_two):
        merged_list[k] = ordered_list_two[j]
        k += 1
        j += 1

    return merged_list
