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
    def search(self, nums: List[int], target: int) -> int:
        index_left = 0
        index_right = len(nums) - 1

        while index_left <= index_right:
            index_middle = (index_left + index_right) // 2
            num_left = nums[index_left]
            num_right = nums[index_right]
            num_middle = nums[index_middle]

            if target == num_left:
                return index_left
            elif target == num_right:
                return index_right
            elif target == num_middle:
                return index_middle
            elif (
                num_left < num_middle and
                (target < num_left or target > num_middle)
            ) or (
                num_middle < num_right and
                (target > num_middle and target < num_right)
            ):
                index_left = index_middle + 1
                index_right -= 1
            else:
                index_left += 1
                index_right = index_middle - 1

        return -1


if __name__ == '__main__':
    solution = Solution()
    # print(solution.search(nums=[1, 3], target=0))
    # print(solution.search(nums=[4,5,6,7,0,1,2], target=0))
    # print(solution.search(nums=[4,5,6,7,0,1,2], target=3))
    # print(solution.search(nums=[1], target=3))
    # print(solution.search(nums=[1], target=1))
    # print(solution.search(nums=[1, 2, 3, 4], target=5))
    # print(solution.search(nums=[2, 3, 4, 1], target=3.5))
    # print(solution.search(nums=[5, 1, 2, 3, 4], target=1))
    # print(solution.search(nums=[5, 1, 2, 3, 4], target=0))
    # print(solution.search(nums=[1, 2, 3, 4, 5, 6], target=4))
    print(solution.search(nums=[8, 1, 2, 3, 4, 5, 6, 7], target=6))
