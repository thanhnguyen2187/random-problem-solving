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
    def maxArea(self, heights: List[int]) -> int:
        left_index = 0
        right_index = len(heights) - 1

        max_volume = 0
        while left_index < right_index:
            left_height = heights[left_index]
            right_height = heights[right_index]
            height = min(left_height, right_height)
            width = right_index - left_index
            volume = height * width
            max_volume = max(volume, max_volume)

            if left_height <= right_height:
                left_index += 1
            else:
                right_index -= 1

        return max_volume


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea(heights=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
