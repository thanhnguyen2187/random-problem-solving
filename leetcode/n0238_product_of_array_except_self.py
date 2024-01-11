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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = len([num for num in nums if num == 0])
        match zero_count:
            case 0:
                product_ = reduce(
                    lambda result, num: result * num,
                    nums,
                    1,
                )
                return [
                    product_ // num
                    for num in nums
                ]
            case 1:
                product_ = reduce(
                    lambda result, num: result * num,
                    [
                        num
                        for num in nums
                        if num != 0
                    ],
                    1
                )
                return [
                    (
                        0
                        if num != 0
                        else product_
                    )
                    for num in nums
                ]
            case other if other >= 2:
                return list(repeat(0, len(nums)))


if __name__ == '__main__':
    solution = Solution()
