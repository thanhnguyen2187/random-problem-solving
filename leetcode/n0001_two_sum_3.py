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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {
            num: index
            for index, num in enumerate(nums)
        }

        for index, num in enumerate(nums):
            inverted_num = target - num
            inverted_index = nums_dict.get(inverted_num, -1)
            if inverted_index != -1 and inverted_index != index:
                return [index, nums_dict[inverted_num]]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(nums=[3, 2, 4], target=6))
