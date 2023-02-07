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
    combinations,
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
from fractions import Fraction


class DisjointSet:
    tracker: DefaultDict

    def find(self, *items):
        return all([
            self.tracker[item_1] == self.tracker[item_2]
            for item_1, item_2 in zip(items, items[1:])
        ])

    def union(self, *items):
        indexes = {
            self.tracker[item]
            for item in items
        }
        min_index = min(indexes)
        for item in self.tracker.keys():
            if self.tracker[item] in indexes:
                self.tracker[item] = min_index

    def __init__(self):
        self.tracker = defaultdict(lambda: len(self.tracker))


def calculate_slope(point_1: List[int], point_2: List[int]) -> float:
    x1, y1 = point_1
    x2, y2 = point_2
    if x2 - x1 == 0:
        return float("inf")
    return (y2 - y1) / (x2 - x1)


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        mapper = defaultdict(Counter)
        for point_1, point_2 in combinations(points, 2):
            slope = calculate_slope(point_1=point_1, point_2=point_2)
            mapper[tuple(point_1)][slope] += 1
        counter_values = chain.from_iterable(
            counter.values()
            for counter in mapper.values()
        )
        return max(counter_values) + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPoints(points=[[1, 1], [2, 2], [3, 3]]))
    print(solution.maxPoints(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
