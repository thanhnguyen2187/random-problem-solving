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
        num: int,
        nums_dict: Dict[int, int],
        nums_set: Set[int],
    ) -> int:

        if num not in nums_set:
            return nums_dict[num]
        else:
            nums_set.remove(num)
            nums_dict[num] = 1 + self.recurse(
                num=num - 1,
                nums_dict=nums_dict,
                nums_set=nums_set,
            )
            return nums_dict[num]

    def longestConsecutive(
        self,
        nums: List[int],
    ) -> int:

        if len(nums) == 0:
            return 0

        nums_set = {
            num
            for num in nums
        }
        nums_dict = defaultdict(lambda: 0)

        for num in nums:
            self.recurse(
                num=num,
                nums_dict=nums_dict,
                nums_set=nums_set,
            )

        return max(nums_dict.values())


if __name__ == '__main__':
    solution = Solution()
    for nums in [
        [100, 4, 200, 1, 3, 2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
        [],
    ]:
        print(
            solution.longestConsecutive(nums=nums)
        )
