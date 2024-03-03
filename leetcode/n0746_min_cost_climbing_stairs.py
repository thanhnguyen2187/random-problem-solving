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
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        @cache
        def recurse(i: int):
            if i <= 1:
                return cost[i]

            return cost[i] + min(
                recurse(i - 1),
                recurse(i - 2),
            )

        return recurse(len(cost) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs(cost=[10, 15, 20]))
    print(solution.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
