from unittest import TestCase
from chapter_07_sorting_and_searching.selection_sort import selection_sort


class TestOfInsertionSort(TestCase):

    def test_selection_sort(self):
        unordered_list = [5, 2, 1, 8, 3, 6]
        sorted_list = selection_sort(unordered_list)

        self.assertEqual(sorted(unordered_list), sorted_list)
