def insertion_sort(unordered_list: list[int]) -> list[int]:
    copied_input = [e for e in unordered_list]
    length = len(copied_input)

    for i in range(1, length):
        key = copied_input[i]
        j = i - 1
        while j >= 0 and copied_input[j] > key:
            copied_input[j + 1] = copied_input[j]
            j -= 1
        copied_input[j + 1] = key

    return copied_input
