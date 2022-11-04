from chapter_08_tree.node import Node


class Traverse:
    # preorder -> value / left / right
    def preorder(self, node: Node, accm: list[int] = []) -> list[int]:
        if node is not None:
            accm.append(node.data)
            self.preorder(node.left, accm)
            self.preorder(node.right, accm)

        return accm

    # inorder -> left / value / right
    def inorder(self, node: Node, accm: list[int] = []) -> list[int]:
        if node is not None:
            self.inorder(node.left, accm)
            accm.append(node.data)
            self.inorder(node.right, accm)

        return accm

    # postorder -> left / right / value
    def postorder(self, node: Node, accm: list[int] = []) -> list[int]:
        if node is not None:
            self.postorder(node.left, accm)
            self.postorder(node.right, accm)
            accm.append(node.data)

        return accm