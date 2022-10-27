def selection_sort(unsorted_list: list[int]) -> list[int]:
  copy_of_list = [i for i in unsorted_list]

  total_length = len(copy_of_list)

  # outer loop
  for i in range(total_length - 1):
    index_of_minimum_element = i
    
    # inner loop
    for j in range(i + 1, total_length):
      if copy_of_list[j] < copy_of_list[index_of_minimum_element]:
        index_of_minimum_element = j
    
    # swap i'th element and j'th element
    copy_of_list[i], copy_of_list[index_of_minimum_element] = copy_of_list[index_of_minimum_element], copy_of_list[i]

  # return sorted list as a result
  return copy_of_list