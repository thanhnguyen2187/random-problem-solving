import math
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
    combinations,
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
)


class ListNode:
    def __init__(
            self,
            x: int,
            next: Optional['ListNode'] = None,
    ):
        self.val: int = x
        self.next: 'ListNode' = next


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

    def judgeSquareSum(
        self,
        c: int,
    ) -> bool:

        if c <= 2:
            return True

        def is_square(x: int) -> bool:
            return x == math.isqrt(x) ** 2

        sqrt_c = int(math.sqrt(c))

        for a in range(1, sqrt_c + 1):
            b = c - a ** 2
            if is_square(b):
                return True

        return False


if __name__ == '__main__':
    solution = Solution()

    for c in [
        # 10, 20, 10001, 131313,
        # 5, 3, 4, 2, 1,
        # 2,
        131313, 999,
    ]:
        print(
            solution.judgeSquareSum(c=c)
        )
