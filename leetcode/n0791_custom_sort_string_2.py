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
    def customSortString(self, order: str, s: str) -> str:
        char_to_index = {
            char: index
            for index, char in enumerate(order)
        }
        result = ''.join(
            sorted(s, key=lambda char: char_to_index.get(char, -1))
        )
        return result


if __name__ == '__main__':
    solution = Solution()
