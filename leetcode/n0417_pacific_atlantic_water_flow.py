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
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        def valid_i_j(i: int, j: int):
            return 0 <= i < m and 0 <= j < n

        origin_1 = set(
            chain(
                ((0, j) for j in range(n)),
                ((i, 0) for i in range(m)),
            )
        )
        flow_1 = set()
        visited = set()
        for i, j in origin_1:
            dq = deque([(i, j)])
            while len(dq) > 0:
                i, j = dq.pop()
                visited.add((i, j))
                flow_1.add((i, j))

                for k, l in (
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                ):
                    if (
                        valid_i_j(i=k, j=l) and
                        (k, l) not in visited and
                        (k, l) not in origin_1 and
                        heights[k][l] >= heights[i][j]
                    ):
                        dq.append((k, l))

        origin_2 = set(
            chain(
                ((i, n - 1) for i in range(m)),
                ((m - 1, j) for j in range(n)),
            )
        )
        flow_2 = set()
        visited = set()
        for i, j in origin_2:
            dq = deque([(i, j)])
            while len(dq) > 0:
                i, j = dq.pop()
                visited.add((i, j))
                flow_2.add((i, j))

                for k, l in (
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                ):
                    if (
                        valid_i_j(i=k, j=l) and
                        (k, l) not in visited and
                        (k, l) not in origin_2 and
                        heights[k][l] >= heights[i][j]
                    ):
                        dq.append((k, l))

        return flow_1.intersection(flow_2)
        # return flow_1


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.pacificAtlantic(
            heights=[
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ]
        )
    )
