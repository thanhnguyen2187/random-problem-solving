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
    def buildTree(
        self,
        preorder: List[int],
        inorder: List[int],
    ) -> TreeNode:
        def recurse(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            if len(preorder) == 0:
                return None

            if len(preorder) != len(inorder):
                raise Exception('buildTree.recurse unreachable code')

            # We find `root` base on this observation: `preorder` always
            # in the form `[root_value, ...left_values, ...right_values]`.
            root_value = preorder[0]
            root = TreeNode(val=root_value)

            # We find `root.left` and `root.right` base on these observations:
            #
            # - `inorder` always in the form `[...left_values, root_value,
            # ...right_values]`.
            # - The problem's description stated that values within the tree are
            # unique. It means after we have `root_value`, we are always able
            # to find `left_node`'s `left_values` and `right_node`'s
            # `right_values` within `inorder`.
            # - `inorder.left_values` and `inorder.right_values` should have the
            # same number of elements as `preorder.left_values` and
            # `preorder.right_values`.
            root_index = inorder.index(root_value)

            root.left = recurse(preorder=preorder[1:root_index + 1], inorder=inorder[:root_index])
            root.right = recurse(preorder=preorder[root_index + 1:], inorder=inorder[root_index + 1:])

            return root

        return recurse(preorder=preorder, inorder=inorder)



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
