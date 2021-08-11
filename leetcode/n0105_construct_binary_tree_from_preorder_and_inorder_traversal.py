from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Union,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    accumulate,
    chain,
    cycle,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
)


class ListNode:
    def __init__(
            self,
            x: int,
            next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: 'TreeNode' = None,
        right: 'TreeNode' = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def build(
        self,
        preorder: List[int],
        inorder: List[int],
    ) -> Optional[TreeNode]:

        if len(preorder) == 0:
            return None

        root_value = preorder[0]
        root = TreeNode(val=root_value)

        root_index = next(
            index
            for index, value in enumerate(inorder)
            if value == root_value
        )
        root.left = self.build(
            preorder=preorder[1:root_index + 1],
            inorder=inorder[0:root_index],
        )
        root.right = self.build(
            preorder=preorder[root_index + 1:],
            inorder=inorder[root_index + 1:],
        )

        return root


    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int],
    ) -> TreeNode:
        return self.build(
            preorder=preorder,
            inorder=inorder,
        )


def convert_tree(
    root: TreeNode,
) -> List[int]:

    if root is None:
        return [None]
    else:
        return [
            root.val,
            *convert_tree(root=root.left),
            *convert_tree(root=root.right),
        ]


if __name__ == '__main__':
    solution = Solution()
    for preorder, inorder in [
        (
            [3, 9, 20, 15, 7],
            [9, 3, 15, 20, 7],
        ),
    ]:
        result = solution.buildTree(
            preorder=preorder,
            inorder=inorder,
        )
        print(
            convert_tree(root=result)
        )
