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


@cache
def pow(x: float, n: int):
    if n == 0:
        return 1
    if n == 1:
        return x

    return pow(x, n // 2) * pow(x, n // 2) * pow(x, n % 2)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / pow(x, -n)
        return pow(x, n)


if __name__ == '__main__':
    solution = Solution()
