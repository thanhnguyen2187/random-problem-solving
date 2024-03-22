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
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: (point[1], point[0]))

        merged_points = [points[0]]
        for point_a in points[1:]:
            point_b = merged_points[-1]
            i, j = point_a
            k, l = point_b

            if i > k:
                i, j, k, l = k, l, i, j

            if i <= k <= j:
                merged_points[-1] = [min(i, k), min(j, l)]
            else:
                merged_points.append((k, l))

        return len(merged_points)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMinArrowShots(points=[[10,16],[2,8],[1,6],[7,12]]))
    print(solution.findMinArrowShots(points=[[1, 2], [3, 4], [5, 6], [7, 8]]))
    print(solution.findMinArrowShots(points=[[1, 2], [2, 3], [3, 4], [4, 5]]))
