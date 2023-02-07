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
    cache,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


@cache
def calculate_tribonacci(n: int):
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 1
        case _:
            return sum((
                calculate_tribonacci(n - 1),
                calculate_tribonacci(n - 2),
                calculate_tribonacci(n - 3),
            ))


class Solution:
    def tribonacci(self, n: int) -> int:
        return calculate_tribonacci(n=n)


if __name__ == '__main__':
    solution = Solution()
