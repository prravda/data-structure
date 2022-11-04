import math


def binary_search_recursive(
        elements: list[int],
        element_to_find: int,
        start_index: int,
        end_index: int
):
    mid_index = math.floor((start_index + end_index) / 2)

    if start_index >= end_index:
        return None

    if element_to_find == elements[mid_index]:
        return mid_index

    if element_to_find > elements[mid_index]:
        return binary_search_recursive(
            elements,
            element_to_find,
            mid_index + 1,
            end_index
        )

    if element_to_find < elements[mid_index]:
        return binary_search_recursive(
            elements,
            element_to_find,
            start_index,
            mid_index - 1,
        )


list_to_test = [1, 2, 3, 4, 5, 6, 7, 8, 9]

index = binary_search_recursive(
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    2,
    0,
    len(list_to_test),
)

print(index)