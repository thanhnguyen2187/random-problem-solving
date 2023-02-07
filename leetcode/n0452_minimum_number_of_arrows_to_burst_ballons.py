from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Union,
    Tuple,
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
)


def iterate(
    current_cursor: int,
    arrow_count: int,
    points: List[List[int]],
) -> Tuple[int, int, List[List[int]]]:
    if points:
        point = points[0]
        if point[0] <= current_cursor:
            return (
                current_cursor,
                arrow_count,
                points[1:],
            )
        else:
            return (
                point[1],
                arrow_count + 1,
                points[1:],
            )
    return (
        current_cursor,
        arrow_count,
        points,
    )


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda point: point[1])
        current_cursor = points[0][1]
        arrow_count = 1

        for point in points:
            if current_cursor >= point[0]:
                continue
            else:
                current_cursor = point[1]
                arrow_count += 1

        return arrow_count


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]]))
    # print(solution.findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))
    # print(solution.findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))
    # print(solution.findMinArrowShots(points=[[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]))
    print(solution.findMinArrowShots(points=[[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]))
