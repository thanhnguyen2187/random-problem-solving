import heapq

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


def distance(p1, p2):
    i, j = p1
    k, l = p2
    return abs(k - i) + abs(l - j)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = defaultdict(set)

        for i, j in permutations(range(n), 2):
            graph[i].add(j)
            graph[j].add(i)

        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (0, 0))
        distances = {}
        result = 0
        while len(pq) > 0:
            d, i = heapq.heappop(pq)
            if i in distances:
                continue
            distances[i] = d
            result += d
            for j in graph[i]:
                if j in distances:
                    continue
                d_ = distance(points[i], points[j])
                heapq.heappush(pq, (d_, j))

        return result


if __name__ == '__main__':
    solution = Solution()
    # points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    # points = [[3, 12], [-2, 5], [-4, 1]]
    # points = [[0, 0]]
    points = [[2, -3], [-17, -8], [13, 8], [-17, -15]]

    print(solution.minCostConnectPoints(points=points))
