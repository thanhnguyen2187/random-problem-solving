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
    combinations,
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
    Counter,
)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        index_left = 0
        index_right = len(nums) - 1

        while nums[index_left] > nums[index_right]:
            # Without this special case handling, the code would run into an
            # infinite loop when there are two elements next to each other.
            #
            # For example, in case `nums = [2, 1]`:
            #
            # ```
            # index_left = 0
            # index_right = 1
            # index_middle = 0
            # ```
            #
            # Then `index_left = index_middle`, and it would be repeated all
            # over again.
            if index_left == index_right - 1:
                return nums[index_right]
            index_middle = (index_left + index_right) // 2

            if nums[index_left] > nums[index_middle]:
                index_right = index_middle
            else:
                index_left = index_middle

        return nums[index_left]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMin(nums=[1, 2, 3, 4, 5]))
    print(solution.findMin(nums=[5, 1, 2, 3, 4]))
    print(solution.findMin(nums=[4, 5, 1, 2, 3]))
    print(solution.findMin(nums=[3, 4, 5, 1, 2]))
    print(solution.findMin(nums=[2, 3, 4, 5, 1]))
