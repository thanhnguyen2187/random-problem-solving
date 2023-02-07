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
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_substrings = [
            s[index:index + len(p)]
            for index in range(len(s) + 1 - len(p))
        ]
        p_sorted = sorted(p)
        result = [
            index
            for index, substring in enumerate(s_substrings)
            if sorted(substring) == p_sorted
        ]
        return result


if __name__ == '__main__':
    solution = Solution()
