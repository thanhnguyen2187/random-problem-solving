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
    reduce,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product_ = reduce(lambda x, y: x * y, nums)
        if product_ > 0:
            return 1
        elif product_ < 0:
            return -1
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
