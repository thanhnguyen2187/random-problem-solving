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
    cache,
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1, *nums, 1]

        @cache
        def recurse(l: int, r: int):
            if l > r:
                return 0
            if r == l:
                return nums[l - 1] * nums[l] * nums[l + 1]

            max_result = 0
            for i in range(l, r + 1):
                result = nums[l - 1] * nums[i] * nums[r + 1]
                result += recurse(l=l, r=i - 1)
                result += recurse(l=i + 1, r=r)
                max_result = max(max_result, result)

            return max_result

        return recurse(l=1, r=len(nums) - 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxCoins(nums=[3, 1, 5, 8]))
    print(solution.maxCoins(nums=[1, 5]))
