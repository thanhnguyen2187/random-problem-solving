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
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, heights[0])]
        max_area = 0
        for i in range(0, len(heights)):
            min_j = i

            while len(stack) > 0:
                j, top = stack[-1]
                if heights[i] < top:
                    min_j = j
                    area = top * (i - j)
                    max_area = max(max_area, area)
                    stack.pop()
                else:
                    break

            stack.append((min_j, heights[i]))

        for i in range(len(stack)):
            j, h = stack[i]
            max_area = max(
                max_area,
                (len(heights) - j) * h,
            )

        return max_area


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea(heights=[4, 2, 2, 2, 2, 4, 4, 2, 2]))
