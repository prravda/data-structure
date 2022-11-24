from chapter_09_search_tree.bst_node import BinarySearchTreeNode
from typing import Optional


class BinarySearchTreeUtilities:
    def search_by_key(self, node: Optional[BinarySearchTreeNode], key: int) -> Optional[BinarySearchTreeNode]:
        if node is None:
            return None

        if key == node.key:
            return node

        if key < node.key:
            return self.search_by_key(node.left, key)

        if key > node.key:
            return self.search_by_key(node.right, key)

    def search_by_value(self, node: Optional[BinarySearchTreeNode], value: int) -> Optional[BinarySearchTreeNode]:
        if node is None:
            return None

        if value == node.value:
            return node

        if value < node.value:
            return self.search_by_value(node.left, value)

        if value > node.right:
            return self.search_by_value(node.right, value)

    def get_minium_key_node_iter(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        node_for_returning = node

        while node_for_returning is not None and node_for_returning.left is not None:
            node_for_returning = node_for_returning.left

        return node_for_returning

    def get_maximum_key_node_iter(self, node: BinarySearchTreeNode) -> BinarySearchTreeNode:
        node_for_returning = node

        while node_for_returning is not None and node_for_returning.right is not None:
            node_for_returning = node_for_returning.right

        return node_for_returning

    # practice 9-1, implement this traversing with recursively
    def get_minimum_key_node_recursively(self, node: Optional[BinarySearchTreeNode]) -> BinarySearchTreeNode:
        if node is not None and node.left is None:
            return node

        if node is not None and node.left is not None:
            return self.get_minimum_key_node_recursively(node.left)

    def get_maximum_key_node_recursively(self, node: Optional[BinarySearchTreeNode]) -> BinarySearchTreeNode:
        if node is not None and node.left is None:
            return node

        if node is not None and node.right is not None:
            return self.get_minimum_key_node_recursively(node.left)

    def insert_by_key(self, node: Optional[BinarySearchTreeNode], key: int) -> None:
        # basically, it should throw(raise) an error
        # cuz binary search tree doesn't allow the duplicates.
        if key == node.key:
            return None

        if key > node.key:
            if node.right is not None:
                return self.insert_by_key(node.right, key)
            if node.right is None:
                node.right = BinarySearchTreeNode(key)
                return

        if key < node.key:
            if node.left is not None:
                return self.insert_by_key(node.left, key)
            if node.left is None:
                node.left = BinarySearchTreeNode(key)
                return

    def delete_by_key(self):
        # TODO: implement the method: delete a node by key and re-arrange the node after deletion