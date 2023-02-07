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
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        reachable = defaultdict(dict)
        for from_, to, price in flights:
            reachable[from_][to] = price

        nodes_queue = deque([(src, 0)])
        distances = list(repeat(float("inf"), n))
        while len(nodes_queue) > 0 and k >= 0:
            current_node_count = len(nodes_queue)
            for _ in range(current_node_count):
                node, distance = nodes_queue.popleft()
                for neighbor_node, neighbor_distance in reachable[node].items():
                    new_distance = distance + neighbor_distance
                    if new_distance < distances[neighbor_node]:
                        distances[neighbor_node] = new_distance
                        nodes_queue.append((neighbor_node, new_distance))
            k -= 1

        return (
            -1
            if distances[dst] == float("inf")
            else distances[dst]
        )


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.findCheapestPrice(
            n=4,
            flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            src=0,
            dst=3,
            k=1,
        )
    )
    print(
        solution.findCheapestPrice(
            n=3,
            flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]],
            src=0,
            dst=2,
            k=1,
        )
    )
