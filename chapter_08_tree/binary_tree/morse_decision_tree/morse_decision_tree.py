from chapter_08_tree.node import Node

class MorseDecisionTree:

    def create_tree_from_codetable(self, code_table: dict[str, str]) -> Node:
        for alphabet in code_table:
            current_morse_code = code_table[alphabet]
            decision_tree = Node()
            current_location = decision_tree
            for c in current_morse_code:
                if c == '-':
                    if current_node.left is None:
                        current_node.left = Node()
                        current_node = current_node.left

                if c == '.':
