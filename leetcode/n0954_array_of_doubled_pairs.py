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
    Counter,
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

    def canReorderDoubled(
        self,
        arr: List[int],
    ) -> bool:

        # arr.sort(key=lambda x: abs(x))
        arr.sort()
        free_numbers = Counter(arr)

        for number in arr:
            if (
                (
                    free_numbers[number] > 0 and
                    free_numbers[2 * number] > 0
                )
            ):
                free_numbers[number] -= 1
                free_numbers[2 * number] -= 1

        return all(
            number == 0
            for number in free_numbers.values()
        )


if __name__ == '__main__':
    solution = Solution()
