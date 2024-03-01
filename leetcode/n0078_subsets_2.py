from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Tuple,
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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recurse(i: int, current: Tuple):
            if i == len(nums):
                result.append(current)
                return

            recurse(i=i + 1, current=current)
            recurse(i=i + 1, current=(*current, nums[i]))

        recurse(i=0, current=())
        return result



if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets(nums=[1, 2, 3]))
