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
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = list(repeat(float("inf"), n))
        temps = list(repeat(float("inf"), n))
        distances[src] = 0
        temps[src] = 0
        for _ in range(k + 1):
            for u, v, w in flights:
                if distances[u] == float("inf"):
                    continue
                temps[v] = min(temps[v], w + distances[u])
            distances = temps.copy()

        if distances[dst] == float("inf"):
            return -1

        return distances[dst]


if __name__ == '__main__':
    solution = Solution()
    # flights = [
    #     [0, 1, 100], [1, 2, 100], [2, 0, 100],
    #     [1, 3, 600], [2, 3, 200],
    # ]
    # n = 4
    # src = 0
    # dst = 3
    # k = 1
    # flights = [
    #     [0, 1, 5], [1, 2, 5], [0, 3, 2],
    #     [3, 1, 2], [1, 4, 1], [4, 2, 1],
    # ]
    # n, src, dst, k = 5, 0, 2, 2
    flights = [
        [0, 1, 1], [0, 2, 5], [1, 2, 1],
        [2, 3, 1],
    ]
    n, src, dst, k = 4, 0, 3, 1
    print(solution.findCheapestPrice(
        n=n,
        flights=flights,
        src=src,
        dst=dst,
        k=k,
    ))
