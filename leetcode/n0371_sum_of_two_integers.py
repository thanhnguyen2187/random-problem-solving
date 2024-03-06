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
    zip_longest,
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
    def getSum(self, a: int, b: int) -> int:
        a += b

        return a


if __name__ == '__main__':
    solution = Solution()
    # print(solution.getSum(a=1, b=2))
    # print(solution.getSum(a=3, b=2))
    print(solution.getSum(a=10, b=11))
    print(solution.getSum(a=-1, b=11))
