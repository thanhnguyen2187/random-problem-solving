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
    def reverse(self, x: int) -> int:
        neg = -1 if x < 0 else 1
        x_str = str(abs(x))
        x_str_rev = list(reversed(x_str))
        result = int(''.join(x_str_rev))
        result *= neg
        if not (-(2**31) < result < (2**31) - 1):
            return 0
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(x=123))
    print(solution.reverse(x=-123))
