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
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in reversed(range(len(digits))):
            if carry:
                digits[i] += 1
                carry = False
            if digits[i] == 10:
                digits[i] = 0
                carry = True

        if carry:
            digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne(digits=[1, 2, 3]))
    print(solution.plusOne(digits=[9, 9, 9]))
