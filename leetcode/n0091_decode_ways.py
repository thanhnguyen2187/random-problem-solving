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
        def recurse(i: int) -> int:
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0

            result: int = 0
            if '1' <= s[i] <= '9':
                result = recurse(i + 1)
            if (
                i + 1 < len(s) and
                (
                    s[i] == '1' or
                    s[i] == '2' and '0' <= s[i + 1] < '7'
                )
            ):
                result += recurse(i + 2)

            return result

        return recurse(0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings(s="12"))
    print(solution.numDecodings(s="226"))
    print(solution.numDecodings(s="06"))
