from unittest import TestCase
from chapter_08_tree.heap_tree.heap_tree_refactored import HeapTreeRefactored

data_to_insert = [2, 5, 4, 8, 9, 3, 7, 3]

expected_result_after_insertion = [9, 8, 7, 3, 5, 3, 4, 2]

expected_result_after_one_deletion = [8, 5, 7, 3, 2, 3, 4]
expected_result_after_two_deletion = [7, 5, 4, 3, 2, 3]


class TestMaxHeapTree(TestCase):

    def test_insert(self):
        max_heap = HeapTreeRefactored()

        for i in data_to_insert:
            max_heap.insert(i)

        self.assertEqual(max_heap.get_element(), expected_result_after_insertion)

    def test_delete(self):

        max_heap = HeapTreeRefactored()

        for i in data_to_insert:
            max_heap.insert(i)

        max_heap.delete()
        self.assertEqual(max_heap.get_element(), expected_result_after_one_deletion)

        max_heap.delete()
        self.assertEqual(max_heap.get_element(), expected_result_after_two_deletion)

