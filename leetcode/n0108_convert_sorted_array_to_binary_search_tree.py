from typing import (
    List,
    Optional,
    Union,
    NamedTuple,
    Dict,
    Set,
    Iterator,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    product,
    cycle,
    repeat,
    islice,
    chain,
    accumulate,
    takewhile,
    permutations,
)
from functools import (
    cached_property,
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

    def insert(
        self,
        root: Optional[TreeNode],
        value: int,
    ) -> TreeNode:

        if root is None:
            return TreeNode(val=value)
        elif value < root.val:
            if root.left is None:
                root.left = self.insert(root=None, value=value)
            else:
                self.insert(root=root.left, value=value)
        else:
            if root.right is None:
                root.right = self.insert(root=None, value=value)
            else:
                self.insert(root=root.right, value=value)

    def generate_indices(
        self,
        indices: List[int],
    ) -> List[int]:

        if len(indices) in (1, 2):
            return indices
        else:
            middle = len(indices) // 2
            return [
                indices[middle],
                *self.generate_indices(
                    indices=indices[0:middle],
                ),
                *self.generate_indices(
                    indices=indices[middle + 1:],
                ),
            ]


    def sortedArrayToBST(
        self,
        nums: List[int],
    ) -> TreeNode:

        indices = self.generate_indices(
            indices=[
                index
                for index in range(len(nums))
            ]
        )
        root = self.insert(
            root=None,
            value=nums[indices[0]],
        )
        for index in indices[1:]:
            self.insert(
                root=root,
                value=nums[index],
            )

        return root



if __name__ == '__main__':
    solution = Solution()
    for nums in [
        [0, 1, 2, 3, 4, 5],
        [0, 1, 2, 3, 4, 5, 6],
    ]:
        print(
            solution.sortedArrayToBST(nums=nums)
        )
