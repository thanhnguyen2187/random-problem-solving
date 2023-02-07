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
    groupby,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


def find_max_subarray_sum(nums: List[int]) -> int:
    results = [nums[0]]
    for num in nums[1:]:
        result = max(results[-1] + num, num)
        results.append(result)

    return max(results)


def find_min_subarray_sum(nums: List[int]) -> int:
    results = [0]
    for num in nums[1:]:
        result = min(results[-1] + num, num)
        results.append(result)

    return min(results)


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        return max(
            find_max_subarray_sum(nums=nums),
            nums_sum - find_min_subarray_sum(nums=nums),
        )


if __name__ == '__main__':
    solution = Solution()
    # print(solution.maxSubarraySumCircular(nums=[1, -2, 3, -2]))
    # print(solution.maxSubarraySumCircular(nums=[5, -3, 5]))
    print(solution.maxSubarraySumCircular(nums=[-3, -2, -3]))
