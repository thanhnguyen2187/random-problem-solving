from typing import (
    Callable,
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

    def count(
        self,
        string: str,
        predicate: Callable[[str], int],
    ) -> List[int]:

        result = [0]
        for character in string:
            result.append(
                result[-1] + (
                    1
                    if predicate(character)
                    else 0
                )
            )

        return result

    def minFlipsMonoIncr(
        self,
        s: str,
    ) -> int:

        ones_count_left_to_right = (
            self.count(
                string=s,
                predicate=lambda character: character == "1",
            )
        )
        zeroes_count_right_to_left = reversed(
            self.count(
                string="".join(reversed(s)),
                predicate=lambda character: character == "0",
            )
        )

        return min(
            one_flip_count + zero_flip_count
            for one_flip_count, zero_flip_count in zip(
                ones_count_left_to_right, zeroes_count_right_to_left,
            )
        )


if __name__ == '__main__':
    solution = Solution()
    for s in [
        "00011000",
        "1010111010101000101",
        "101010100010101000101111110101111010",
        "1000001011111111010",
        "00110",
        "10111001010",
    ]:
        print(
            solution.minFlipsMonoIncr(s=s)
        )
