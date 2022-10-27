def selection_sort(unsorted_list: list[int]) -> list[int]:
  total_length = len(unsorted_list)

  # outer loop
  for i in range(total_length - 1):
    index_of_minimum_element = i
    
    # inner loop
    for j in range(i + 1, total_length):
      if unsorted_list[j] < unsorted_list[i]:
        index_of_minimum_element = j
    
    # swap i'th element and j'th element
    unsorted_list[i], unsorted_list[index_of_minimum_element] = unsorted_list[index_of_minimum_element], unsorted_list[i]
    print(f"step: {i + 1}th \n current status: {unsorted_list}")

  # return sorted list as a result
  return unsorted_list

unordered_list = [5, 3, 2, 9, 7, 1]
print(selection_sort(unordered_list))