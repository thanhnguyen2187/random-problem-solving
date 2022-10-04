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
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        max_left = max(
            left + height
            for position in positions
            for left, height in position
        )
        current_heights = [
            0
            for _ in range(max_left + 1)
        ]
        
        for position in positions:
            for left, height in position:
                current_heights[left:left + height] += height

        return max(current_heights)


if __name__ == '__main__':
    solution = Solution()
