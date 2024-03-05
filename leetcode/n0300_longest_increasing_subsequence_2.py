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
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        results = list(repeat(1, n))

        for i in reversed(range(0, n - 1)):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    results[i] = max(results[i], results[j] + 1)

        return max(results)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.lengthOfLIS(nums=[1, 2, 3, 4, 1, 3, 5, 5, 6, 7, 8]))
    print(solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
