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
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(set)
        for node, parent_node in enumerate(parent):
            tree[parent_node].add(node)

        result = 1

        # noinspection PyShadowingNames
        def dfs(node: int) -> int:
            nonlocal result
            child_lengths = [
                (child_node, dfs(node=child_node))
                for child_node in tree[node]
            ]
            valid_child_lengths = [
                length
                for child_node, length in child_lengths
                if s[node] != s[child_node]
            ]
            valid_child_lengths = sorted(valid_child_lengths)
            result = max(result, sum(valid_child_lengths[-2:]) + 1)
            if valid_child_lengths:
                return valid_child_lengths[-1] + 1
            else:
                return 1

        dfs(0)

        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.longestPath(parent=[-1, 0, 0, 1, 1, 2], s="abacbe"))
    # print(solution.longestPath(parent=[-1, 0, 0, 0], s="aabc"))
    # print(solution.longestPath(parent=[-1, 0], s="mm"))
    # print(solution.longestPath(parent=[-1], s="z"))
    print(solution.longestPath(parent=[-1, 0, 1], s="aab"))
