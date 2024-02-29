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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def recurse(i: int, current: tuple):
            if i >= len(nums):
                result.add(tuple(sorted(current)))
                return

            num = nums[i]
            recurse(i=i + 1, current=current)
            recurse(i=i + 1, current=(*current, num))

        recurse(i=0, current=())

        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.subsetsWithDup(nums=[1, 2, 2]))
    print(solution.subsetsWithDup(nums=[4, 4, 4, 1, 4]))

    # [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]
    # [[4, 1], [4, 1, 4], [4, 4, 1], [4, 4, 1, 4], [4, 4, 4, 1], [4, 4, 4, 1, 4]]
    # [[1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], ]
