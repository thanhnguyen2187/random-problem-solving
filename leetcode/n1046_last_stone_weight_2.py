import bisect

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
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone_1, stone_2 = stones.pop(), stones.pop()
            new_stone = stone_1 - stone_2
            if new_stone > 0:
                bisect.insort(stones, new_stone)

        return (
            stones[0]
            if len(stones) > 0
            else 0
        )


if __name__ == '__main__':
    solution = Solution()
