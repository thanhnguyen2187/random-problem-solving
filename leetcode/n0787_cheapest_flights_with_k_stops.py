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
        graph = defaultdict(dict)
        for i, j, price in flights:
            graph[i][j] = price

        cheapest_price = float("inf")
        visited = set()
        def recurse(i: int, count: int, current: int):
            nonlocal cheapest_price
            if i in visited:
                return
            if count > k + 2:
                return
            if i == dst:
                cheapest_price = min(cheapest_price, current)
                return

            visited.add(i)
            for j in graph[i]:
                recurse(i=j, count=count + 1, current=current + graph[i][j])
            visited.remove(i)

        recurse(i=src, count=1, current=0)

        if cheapest_price == float("inf"):
            return -1

        return cheapest_price


if __name__ == '__main__':
    solution = Solution()
    # n = 4
    # flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    # src = 0
    # dst = 3
    # k = 1
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    print(solution.findCheapestPrice(n=n, flights=flights, src=src, dst=dst, k=k))
