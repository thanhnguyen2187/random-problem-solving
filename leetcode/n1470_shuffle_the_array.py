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


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [
            element
            for pair in zip(nums[:n], nums[n:])
            for element in pair
        ]


if __name__ == '__main__':
    solution = Solution()
