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
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjacency_list = defaultdict(set)
        answers = list(repeat(0, n))
        for edge in edges:
            from_, to = edge
            adjacency_list[from_].add(to)
            adjacency_list[to].add(from_)

        def dfs(parent_node: int, node: int) -> Counter:
            counter = Counter()
            for child_node in adjacency_list[node]:
                if child_node != parent_node:
                    counter += dfs(parent_node=node, node=child_node)
            counter[labels[node]] += 1
            answers[node] = counter[labels[node]]
            return counter

        dfs(-1, 0)

        return answers


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.countSubTrees(
            n=7,
            edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            labels="abaedcd",
        )
    )
    print(
        solution.countSubTrees(
            n=4,
            edges=[[0, 1], [1, 2], [0, 3]],
            labels="bbbb",
        )
    )
