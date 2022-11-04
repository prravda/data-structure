from chapter_08_tree.node import *

tree_example = Node(1)
tree_example.left = Node(2)
tree_example.right = Node(3)
tree_example.left.left = Node(4)
tree_example.left.right = Node(5)
tree_example.right.left = Node(6)
tree_example.right.right = Node(7)


preorder_expectation = [1, 2, 4, 5, 3, 6, 7]
inorder_expectation = [4, 2, 5, 1, 6, 3, 7]
postorder_expectation = [4, 5, 2, 6, 7, 3, 1]
