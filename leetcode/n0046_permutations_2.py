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
    def permute(self, nums: List[int]) -> List[List[int]]:
        picked = set()
        result = []
        def recurse(current: tuple):
            if len(picked) == len(nums):
                result.append(current)
                return

            for i in range(len(nums)):
                if i in picked:
                    continue
                picked.add(i)
                num = nums[i]
                recurse(current=(*current, num))
                picked.remove(i)

        recurse(current=())

        return result


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.permute(nums=[1, 2, 3])
    )
