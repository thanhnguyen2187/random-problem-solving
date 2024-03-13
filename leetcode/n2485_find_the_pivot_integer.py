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
    def pivotInteger(self, n: int) -> int:
        x = math.sqrt((n * (n + 1)) / 2)
        return int(x) if x.is_integer() else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.pivotInteger(n=1000))
    print(solution.pivotInteger(n=8))
    print(solution.pivotInteger(n=7))
    print(solution.pivotInteger(n=6))
    print(solution.pivotInteger(n=5))
    print(solution.pivotInteger(n=4))
    print(solution.pivotInteger(n=3))
    print(solution.pivotInteger(n=2))
    print(solution.pivotInteger(n=1))
