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
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


def redistribute(x: int, n: int) -> [int]:
    remainder = x % n
    result = [x // n] * n
    for index in range(1, remainder + 1):
        result[-index] += 1

    return result


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        nums_sums = list(accumulate(nums))
        nums_ns = range(1, len(nums) + 1)
        return max(
            math.ceil(nums_sum / nums_n)
            for nums_sum, nums_n in zip(nums_sums, nums_ns)
        )


if __name__ == '__main__':
    solution = Solution()
    # print(solution.minimizeArrayValue(nums=[3, 7, 1, 6]))
    # print(solution.minimizeArrayValue(nums=[10, 1]))
    print(solution.minimizeArrayValue(nums=[4, 7, 2, 2, 9, 19, 16, 0, 3, 15]))
    print(solution.minimizeArrayValue(
        nums=[439, 228, 482, 150, 231, 209, 991, 125, 453, 407, 670, 491, 300, 125, 285, 749, 350, 411, 527, 768]
    ))
