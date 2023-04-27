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
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        profits = Counter()
        for p in profit:
            for existed_p in list(profits.keys()):
                profits[p + existed_p] += 1
            profits[p] += 1

        profitable = {
            key: value
            for key, value in profits.items()
            if key >= minProfit
        }
        return sum(profitable.values()) % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution()
