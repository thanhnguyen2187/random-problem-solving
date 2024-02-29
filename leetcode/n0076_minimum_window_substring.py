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
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        set_1 = Counter(t)
        l = 0
        r = len(t)
        set_2 = Counter(
            char
            for char in s[l:r]
            if char in set_1
        )
        if set_2 >= set_1:
            return s[l:r]

        min_l, min_r = -1, len(s)
        while r < len(s):
            if s[r] in set_1:
                set_2[s[r]] += 1
            while set_2 >= set_1:
                if s[l] in set_1:
                    set_2[s[l]] -= 1
                if r - l + 1 < min_r - min_l:
                    min_l, min_r = l, r + 1
                l += 1
            r += 1

        if min_l == -1:
            return ""

        return s[min_l:min_r]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow(
        s="ADOBECODEBANCBAAAA",
        t="ABC",
    ))
