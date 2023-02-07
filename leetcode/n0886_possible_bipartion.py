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


class DisjointSet:
    tracker: List[int]

    def find(self, *items) -> bool:
        return all([
            self.tracker[item_1] == self.tracker[item_2]
            for item_1, item_2 in zip(items, items[1:])
        ])

    def union(self, *items):
        index = min([
            self.tracker[item]
            for item in items
        ])
        for item in items:
            self.tracker[item] = index

    def __init__(self, n: int):
        self.tracker = list(range(n))


class Solution:
    def possibleBipartition(
        self,
        n: int,
        dislikes: List[List[int]],
    ) -> bool:
        adjacency_list: DefaultDict[int, Set] = defaultdict(set)
        disjoint_set = DisjointSet(n + 1)
        for a, b in dislikes:
            adjacency_list[a].add(b)
            adjacency_list[b].add(a)

        for node, neighbors in adjacency_list.items():
            disjoint_set.union(*neighbors)

        for node, neighbors in adjacency_list.items():
            if disjoint_set.find(node, *neighbors):
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.possibleBipartition(n=4, dislikes=[[1, 2], [1, 3], [2, 4]]))
    print(solution.possibleBipartition(n=3, dislikes=[[1, 2], [1, 3], [2, 3]]))
    print(solution.possibleBipartition(n=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))
    print(solution.possibleBipartition(n=10, dislikes=[[1, 2], [3, 4], [5, 6], [6, 7], [8, 9], [7, 8]]))
