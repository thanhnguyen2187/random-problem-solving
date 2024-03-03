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
    def climbStairs(self, n: int) -> int:
        @cache
        def recurse(n: int) -> int:
            if n <= 1:
                return 1

            return recurse(n - 1) + recurse(n - 2)

        return recurse(n=n)


if __name__ == '__main__':
    solution = Solution()
