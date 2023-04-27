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
    cached_property,
    cache,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return math.floor(math.sqrt(n))


if __name__ == '__main__':
    solution = Solution()
    print(solution.bulbSwitch(n=3))
