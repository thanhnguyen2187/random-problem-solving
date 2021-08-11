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
        inorder: List[int],
        postorder: List[int],
    ) -> Optional[TreeNode]:

        if len(inorder) == 0:
            return None

        root_value = postorder[-1]
        root = TreeNode(val=root_value)

        root_index = next(
            index
            for index, value in enumerate(inorder)
            if value == root_value
        )
        root.left = self.build(
            inorder=inorder[:root_index],
            postorder=postorder[:root_index],
        )
        root.right = self.build(
            inorder=inorder[root_index + 1:],
            postorder=postorder[root_index:-1],
        )

        return root


    def buildTree(
        self,
        inorder: List[int],
        postorder: List[int],
    ) -> Optional[TreeNode]:
        return self.build(
            inorder=inorder,
            postorder=postorder,
        )


if __name__ == '__main__':
    solution = Solution()
