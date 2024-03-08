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
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = {}
        def recurse(i: int, bought: bool):
            if i >= n:
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]

            price = prices[i]
            if not bought:
                buying = recurse(i=i + 1, bought=True) - price
                waiting = recurse(i=i + 1, bought=False)
                dp[(i, bought)] = max(buying, waiting)
            else:
                selling = recurse(i=i + 2, bought=False) + price
                holding = recurse(i=i + 1, bought=True)
                dp[(i, bought)] = max(selling, holding)
            return dp[(i, bought)]
        recurse(i=0, bought=False)

        return dp[(0, False)]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(prices=[1, 2, 3, 0, 2]))
    # print(solution.maxProfit(prices=[1]))
