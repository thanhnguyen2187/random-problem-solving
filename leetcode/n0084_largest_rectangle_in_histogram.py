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
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, heights[0])]
        max_area = heights[0]

        for index, height in enumerate(heights[1:], 1):
            minimal_index = index
            while len(stack) > 0:
                top_index, top_height = stack[-1]
                if height < top_height:
                    stack.pop()
                    area = top_height * (index - top_index)
                    max_area = max(max_area, area)
                    minimal_index = top_index
                else:
                    break

            stack.append((minimal_index, height))

        for index, height in stack:
            area = height * (len(heights) - index)
            max_area = max(max_area, area)

        return max_area


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
    print(solution.largestRectangleArea(heights=[2, 4]))
    print(solution.largestRectangleArea(heights=[2, 4, 2, 1, 1, 1, 1, 1, 1]))
