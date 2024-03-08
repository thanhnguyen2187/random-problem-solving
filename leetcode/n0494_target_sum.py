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
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # map from `(i, target)` to `count`
        dp = defaultdict(lambda: 0)
        # `(-1, 0)` denotes there is one way to reach `0` with an empty set
        dp[(-1, 0)] = 1
        sum_ = sum(nums)

        def recurse(i: int, current: int):
            if (i, current) in dp:
                return dp[(i, current)]
            if (not 0 <= i < n) or (not -sum_ <= current <= sum_):
                dp[(i, current)] = 0
                return 0

            num = nums[i]
            result = recurse(i - 1, current - num)
            result += recurse(i - 1, current + num)
            dp[(i, current)] = result
            return result

        recurse(i=n - 1, current=target)

        return dp[(n - 1, target)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3))
    print(solution.findTargetSumWays(nums=[1], target=1))
