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
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pos_results = list(repeat(0, n))
        neg_results = list(repeat(0, n))
        pos_results[0] = nums[0]
        neg_results[0] = nums[0]
        for i in range(1, n):
            num = nums[i]
            if num == 0:
                pos_results[i] = 0
                neg_results[i] = 0
                continue
            neg_results[i] = min(
                num,
                num * neg_results[i - 1],
                num * pos_results[i - 1],
            )
            pos_results[i] = max(
                num,
                num * neg_results[i - 1],
                num * pos_results[i - 1],
            )

        return max(pos_results)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.maxProduct(nums=[2, 3, -2, 4]))
    # print(solution.maxProduct(nums=[-2, 3, -4]))
    # print(solution.maxProduct(nums=[-2, 0, -1]))
    # print(solution.maxProduct(nums=[-2, 1, -3]))
    # print(solution.maxProduct(nums=[-1, -2, -9, -6]))
    print(solution.maxProduct(nums=[2, -5, -2, -4, 3]))
