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
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = Counter(
            num % k
            for num in accumulate(nums)
        )
        result = remainders[0]
        result += sum(
            x * (x - 1) // 2
            for x in remainders.values()
        )
        return result


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.subarraysDivByK(
            nums=[4, 5, 0, -2, -3, 1],
            k=5,
        )
    )
