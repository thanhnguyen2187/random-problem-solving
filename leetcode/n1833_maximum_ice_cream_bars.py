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
)


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        total_costs = list(accumulate(costs))
        optimal_number = bisect_right(total_costs, coins)
        return optimal_number


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxIceCream(costs=[1, 3, 2, 4, 1], coins=7))
    print(solution.maxIceCream(costs=[10, 6, 8, 7, 7, 8], coins=5))
    print(solution.maxIceCream(costs=[1, 6, 3, 1, 2, 5], coins=20))
