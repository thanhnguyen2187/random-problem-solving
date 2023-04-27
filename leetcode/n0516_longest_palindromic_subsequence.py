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
    cache,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


@cache
def recurse(s: str) -> int:
    if len(s) <= 1:
        return len(s)
    elif s[0] == s[-1]:
        return 2 + recurse(s[1:-1])
    else:
        return max(
            recurse(s[1:]),
            recurse(s[:-1]),
        )


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return recurse(s=s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindromeSubseq(s="bbbab"))
