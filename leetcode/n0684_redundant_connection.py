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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = list(range(len(edges) + 1))
        ranks = list(repeat(1, len(parents)))

        def find(i: int):
            p = parents[i]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(i: int, j: int):
            pi = find(i)
            pj = find(j)
            if pi == pj:
                return False

            if ranks[pi] > ranks[pj]:
                parents[pj] = pi
            elif ranks[pi] < ranks[pj]:
                parents[pi] = pj
            else:
                parents[pi] = parents[pj]
                ranks[pi] += 1
                ranks[pj] = ranks[pi]

            return True

        for i, j in edges:
            if not union(i=i, j=j):
                return (i, j)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findRedundantConnection(edges=[[1, 2], [1, 3], [2, 3]]))
    # print(
    #     solution.findRedundantConnection(
    #         edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],
    #     )
    # )
