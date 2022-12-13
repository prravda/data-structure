"""
시험범위 공지
- graph 조금 나가고 그냥 끝 (spanning tree, toplogical sort 는 x)
    - bfs, dfs 좀 나감
- undirectional 뿐만 아니라 weight graph, directional 도 다 함
"""


class TreeNode:
    def __init__(
            self,
            data,
            left,
            right
    ):
        self.data = data
        self.left = left
        self.right = right


# 1
root = TreeNode(1)
root_left = TreeNode(2)
root_right = TreeNode(3)

# 2
left_terminal = TreeNode(2)
right_terminal = TreeNode(3)
root = TreeNode(1, left_terminal, right_terminal)


# traversing
"""
pre: v/l/r 
in: l/v/r
post: l/r/v
---
level: traverse the tree by its level
"""

def traverse_in_preorder(root: TreeNode):
    if root is None:
        return None

    print(root.data)

    if root.left is not None:
        traverse_in_preorder(root.left)

    if root.right is not None:
        traverse_in_preorder(root.right)

# reference
def preorder(n):
    if n is not None:
        print(n.data)
        preorder(n.left)
        preorder(n.right)

def get_num_of_total_nodes(root: TreeNode) -> int:
    if root is None:
        return 0

    return 1 + get_num_of_total_nodes(root.left) + get_num_of_total_nodes(root.right)
def inorder(n):
    if n is not None:
        preorder(n.left)
        print(n.data)
        preorder(n.right)
def postorder(n):
    if n is not None:
        preorder(n.left)
        preorder(n.right)
        print(n.data)


