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
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        @cache
        def recurse(amount: int):
            if amount in coins:
                return 1
            elif amount == 0:
                return 0
            elif amount < 0:
                return float("inf")

            result = float("inf")
            for coin in coins:
                result = min(result, 1 + recurse(amount=amount - coin))
            return result

        # recurse(i=0, remain=amount, current=0)
        result = recurse(amount=amount)
        return (
            -1
            if result == float("inf")
            else result
        )


if __name__ == '__main__':
    solution = Solution()
    # print(solution.coinChange(coins=[1, 2, 5], amount=11))
    # print(solution.coinChange(coins=[2], amount=10))
    # print(solution.coinChange(coins=[3], amount=10))
    # print(solution.coinChange(coins=[186, 419, 83, 408], amount=6249))
