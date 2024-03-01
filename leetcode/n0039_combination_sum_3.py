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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def recurse(i: int, target: int, current: tuple):
            if i >= len(candidates):
                return

            new_target = target - candidates[i]
            new_current = (*current, candidates[i])
            if new_target == 0:
                result.append(new_current)
                return
            elif new_target < 0:
                return

            recurse(i=i, target=new_target, current=new_current)
            recurse(i=i + 1, target=new_target, current=new_current)

        for i in range(len(candidates)):
            recurse(i=i, target=target, current=())
        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.combinationSum(
    #     candidates=[2, 3, 6, 7],
    #     target=7,
    # ))
    print(solution.combinationSum(
        candidates=[3, 5, 8],
        target=11,
    ))
