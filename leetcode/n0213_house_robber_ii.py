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
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        def helper(nums: List[int]) -> int:
            n = len(nums)
            result = list(repeat(0, n))
            result[0] = nums[0]
            result[1] = max(nums[0], nums[1])

            for i in range(2, n):
                result[i] = max(
                    nums[i] + result[i - 2],
                    result[i - 1],
                )

            return result[-1]

        return max(
            helper(nums=nums[1:]),
            helper(nums=nums[:-1]),
        )


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob(nums=[2, 3, 2]))
    print(solution.rob(nums=[1, 2, 3, 1]))
    print(solution.rob(nums=[1, 2, 3]))
