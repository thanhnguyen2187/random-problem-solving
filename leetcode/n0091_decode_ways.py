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
    def numDecodings(self, s: str) -> int:
        @cache
        def recurse(s: str) -> int:
            n = len(s)
            if n <= 1:
                return n
            if len(s) == 2:
                x = int(s)
                if 10 <= x <= 26:
                    return 2

                return 1

            return recurse(s[1:]) + recurse(s[:2]) * recurse(s[2:])

        return recurse(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings(s="12"))
    print(solution.numDecodings(s="226"))
