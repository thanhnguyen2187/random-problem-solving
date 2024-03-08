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


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w

        distances = [float("inf") for _ in range(n + 1)]
        pq = []
        heapq.heapify(pq)
        heapq.heappush(pq, (0, k))

        visited = set()
        while len(pq) > 0:
            d, i = heapq.heappop(pq)
            if i in visited:
                continue

            visited.add(i)
            distances[i] = d
            for j in graph[i]:
                if j in visited:
                    continue

                heapq.heappush(pq, (d + graph[i][j], j))

        result = max(distances[1:])
        return result if result != float("inf") else -1


if __name__ == '__main__':
    solution = Solution()
    times = [[1, 2, 1], [1, 3, 3], [2, 3, 4]]
    n = 4
    k = 1
    print(solution.networkDelayTime(times=times, n=n, k=k))
