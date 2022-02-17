import numbers
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

    def create_complex_number(
        self,
        number_str: str,
    ) -> complex:

        split_str = number_str.split("+")
        real = int(split_str[0])
        imag = int(split_str[1][:-1])

        c = complex(real=real, imag=imag)

        return c

    def convert_complex_nuber(
        self,
        number: complex,
    ) -> str:

        return f"{int(number.real)}+{int(number.imag)}i"

    def complexNumberMultiply(
        self,
        num1: str,
        num2: str,
    ) -> str:
        c1 = self.create_complex_number(number_str=num1)
        c2 = self.create_complex_number(number_str=num2)

        return self.convert_complex_nuber(
            number=(c1 * c2)
        )


if __name__ == '__main__':
    solution = Solution()
