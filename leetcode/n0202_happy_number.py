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
def transform(n: int):
    digits = [
        int(digit)
        for digit in str(n)
    ]
    return sum(
        digit * digit
        for digit in digits
    )


class Solution:
    def isHappy(self, n: int) -> bool:
        encountered = {n}

        while n != 1:
            t = transform(n)
            if t in encountered:
                return False
            encountered.add(t)
            n = t

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(n=19))
    print(solution.isHappy(n=2))
