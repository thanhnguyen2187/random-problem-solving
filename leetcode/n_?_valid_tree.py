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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = list(range(n))
        ranks = list(repeat(0, n))

        def find(i: int):
            p = parents[i]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(i: int, j: int):
            p1 = find(i)
            p2 = find(j)

            if p1 == p2:
                return False

            if ranks[p1] < ranks[p2]:
                parents[p1] = parents[p2]
            elif ranks[p1] > ranks[p2]:
                parents[p2] = parents[p1]
            else:
                parents[p1] = parents[p2]
                ranks[p1] += 1
                ranks[p2] = ranks[p1]

            return True

        for i, j in edges:
            if not union(i, j):
                return False

        compressed_parents = set(
            find(i)
            for i in range(n)
        )

        return len(compressed_parents) == 1


if __name__ == '__main__':
    solution = Solution()
