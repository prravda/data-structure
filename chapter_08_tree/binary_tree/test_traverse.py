from unittest import TestCase
from chapter_08_tree.binary_tree.traverse import Traverse
from chapter_08_tree.tree_example import tree_example, preorder_expectation, inorder_expectation, postorder_expectation


class TestTraverse(TestCase):
    def test_preorder(self):
        result = Traverse().preorder(tree_example)
        self.assertEqual(result, preorder_expectation)

    def test_inorder(self):
        result = Traverse().inorder(tree_example)
        self.assertEqual(result, inorder_expectation)

    def test_postorder(self):
        result = Traverse().postorder(tree_example)
        self.assertEqual(result, postorder_expectation)

