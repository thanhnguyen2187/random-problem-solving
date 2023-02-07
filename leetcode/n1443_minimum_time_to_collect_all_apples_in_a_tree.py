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
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def minTime(
        self,
        n: int,
        edges: List[List[int]],
        hasApple: List[bool],
    ) -> int:
        tree = defaultdict(set)
        for edge in edges:
            from_, to = edge
            tree[from_].add(to)
            tree[to].add(from_)
        visited = defaultdict(lambda: False)

        def dfs(node: int) -> (int, bool):
            if visited[node]:
                return 0, False
            visited[node] = True

            has_apple = hasApple[node]
            child_nodes = tree[node]
            pairs = [
                dfs(node=child_node)
                for child_node in child_nodes
            ]
            child_nodes_has_apple = (
                has_apple or
                any(pair[1] for pair in pairs)
            )
            step_count = (
                2 + sum(pair[0] for pair in pairs)
                if child_nodes_has_apple
                else 0
            )
            return step_count, child_nodes_has_apple

        return max(dfs(0)[0] - 2, 0)


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.minTime(
            n=7,
            edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            hasApple=[False, False, True, False, True, True, False],
        )
    )
    print(
        solution.minTime(
            n=7,
            edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            hasApple=[False, False, True, False, False, True, False],
        )
    )
    print(
        solution.minTime(
            n=7,
            edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            hasApple=[False, False, False, False, False, False, False],
        )
    )
