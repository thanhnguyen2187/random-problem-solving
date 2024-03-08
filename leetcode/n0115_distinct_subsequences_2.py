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
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        elif len(t) == len(s):
            return (
                1
                if t == s
                else 0
            )

        m = len(s)
        n = len(t)
        @cache
        def recurse(i: int, j: int):
            if j >= n:
                return 1
            if i >= m:
                return 0

            if s[i] == t[j]:
                return recurse(i=i + 1, j=j) + recurse(i=i + 1, j=j + 1)

            return recurse(i=i + 1, j=j)

        return recurse(i=0, j=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDistinct(s="rabbbit", t="rabbit"))
    print(solution.numDistinct(s="babgbag", t="bag"))
