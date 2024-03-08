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
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        n = amount

        results = [
            [0 for _ in range(n + 1)]
            for _ in range(m + 1)
        ]
        for i in range(m + 1):
            results[i][0] = 1

        for i, j in product(range(1, m + 1), range(1, n + 1)):
            coin = coins[i - 1]
            results[i][j] = results[i - 1][j]
            if j >= coin:
                results[i][j] += results[i][j - coin]

        return results[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.change(amount=5, coins=[1, 2, 5]))
    print(solution.change(amount=3, coins=[2]))
    print(solution.change(amount=10, coins=[10]))
