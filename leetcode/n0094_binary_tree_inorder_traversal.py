from typing import (
    List,
    Optional,
)


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(
        self,
        root: TreeNode,
    ) -> List[int]:
        nodes_stack = [root]
        node_current = root
        node_values = []

        while (
            len(nodes_stack) > 0
        ):
            if node_current is not None:
                nodes_stack.append(node_current)
                node_current = node_current.left
            else:
                node_current = nodes_stack.pop()
                node_values.append(
                    node_current.val
                )
                node_current = node_current.right

        return node_values


def create_tree(
    values: List[int],
) -> TreeNode:
    ...


if __name__ == '__main__':
    solution = Solution()

