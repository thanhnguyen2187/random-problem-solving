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
    def trap(self, heights: List[int]) -> int:
        max_heights_left = [heights[0]]
        for height in heights[1:]:
            max_heights_left.append(max(max_heights_left[-1], height))

        max_heights_right = [heights[-1]]
        for height in reversed(heights[:-1]):
            max_heights_right.append(max(max_heights_right[-1], height))

        max_heights_right.reverse()

        volume = 0
        for height, max_height_left, max_height_right in zip(
            heights,
            max_heights_left,
            max_heights_right,
        ):
            volume += min(max_height_left, max_height_right) - height

        return volume


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap(heights=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(solution.trap(heights=[4, 2, 0, 3, 2, 5]))
