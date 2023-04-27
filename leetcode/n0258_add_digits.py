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


def recurse(num: int) -> int:
    if num < 10:
        return num
    return recurse(sum([
        num % 10,
        num % (10 ** 2) // 10,
        num % (10 ** 3) // (10 ** 2),
        num % (10 ** 4) // (10 ** 3),
        num % (10 ** 5) // (10 ** 4),
        num % (10 ** 6) // (10 ** 5),
        num % (10 ** 7) // (10 ** 6),
        num % (10 ** 8) // (10 ** 7),
        num % (10 ** 9) // (10 ** 8),
        num // (10 ** 9),
    ]))


class Solution:
    def addDigits(self, num: int) -> int:
        return recurse(num)


if __name__ == '__main__':
    solution = Solution()
    print(solution.addDigits(num=39))
