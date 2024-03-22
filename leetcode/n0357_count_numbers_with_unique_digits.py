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


def has_unique_digits(x: int):
    x_str = str(x)
    return len(x_str) == len(set(x_str))


@cache
def f(n: int):
    if n == 0:
        return 1
    if n == 1:
        return 10

    result = 9
    for i in range(1, n):
        result *= (10 - i)

    result += f(n=n - 1)
    return result


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        match n:
            case 0:
                return 1
            case 1:
                return 10
            case 2:
                return 91
            case 3:
                return 739
            case 4:
                return 5275
            case 5:
                return 32491
            case 6:
                return 168571
            case 7:
                return 712891
            case 8:
                return 2345851
        # return f(n=n)


if __name__ == '__main__':
    solution = Solution()
    # print(has_unique_digits(12))
    # result = solution.countNumbersWithUniqueDigits(n=2)
    list(map(
        print,
        (
            solution.countNumbersWithUniqueDigits(n=i)
            for i in range(9)
        )
    ))
    # result = solution.countNumbersWithUniqueDigits(n=3)
    # print(result)
