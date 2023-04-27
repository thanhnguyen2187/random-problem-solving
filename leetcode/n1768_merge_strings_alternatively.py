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
    zip_longest,
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
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(
            char_1 + char_2
            for char_1, char_2 in zip_longest(word1, word2, fillvalue='')
        )


if __name__ == '__main__':
    solution = Solution()
