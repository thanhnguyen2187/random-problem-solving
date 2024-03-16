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


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        accumulated = list(chain((0,), accumulate(nums)))
        counter = Counter()

        result = 0
        for a in accumulated:
            result += counter[a - goal]
            counter[a] += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numSubarraysWithSum(nums=[1, 0, 1, 0, 1], goal=2))
    print(solution.numSubarraysWithSum(nums=[0, 0, 0, 0, 0], goal=0))
    print(solution.numSubarraysWithSum(nums=[1, 1, 1, 1, 1], goal=2))
