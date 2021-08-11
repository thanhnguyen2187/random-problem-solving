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

    def recurse(
        self,
        nums: List[int],
        start: int,
        temp: List[int],
        result: List[List[int]],
    ):
        result.append(temp.copy())

        for index in range(start, len(nums)):
            if (
                index > start and
                nums[index] == nums[index - 1]
            ):
                continue

            temp.append(nums[index])
            self.recurse(
                nums=nums,
                start=index + 1,
                temp=temp,
                result=result,
            )
            temp.pop()

    def subsetsWithDup(
        self,
        nums: List[int]
    ) -> List[List[int]]:

        nums.sort()

        result = []
        self.recurse(
            nums=nums,
            start=0,
            temp=[],
            result=result,
        )

        return result


if __name__ == '__main__':
    solution = Solution()
