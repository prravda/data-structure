from unittest import TestCase
from chapter_07_sorting_and_searching.insertion_sort import insertion_sort

class TestOfInsertionSort(TestCase):

  def does_it_sorted_well_with_insertion_sort():
    unordered_list = [5, 2, 1, 8, 3, 6]
    sorted_list = insertion_sort(unordered_list)

    self.assertEquals(unordered_list, sorted_list)
