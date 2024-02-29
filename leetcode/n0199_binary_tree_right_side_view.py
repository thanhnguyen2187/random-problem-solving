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


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: 'TreeNode' = None,
        right: 'TreeNode' = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def recurse(root: Optional[TreeNode], level: int, result: dict):
            if root is None:
                return

            result[level] = root.val
            recurse(root=root.left, level=level + 1, result=result)
            recurse(root=root.right, level=level + 1, result=result)

        result_dict = {}
        recurse(root=root, level=0, result=result_dict)

        result = []
        level = 0
        while level in result_dict:
            result.append(result_dict[level])
            level += 1

        return result


if __name__ == '__main__':
    solution = Solution()
