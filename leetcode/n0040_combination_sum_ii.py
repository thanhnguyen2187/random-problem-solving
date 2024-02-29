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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def recurse(i: int, remain: int, current: tuple):
            if remain == 0:
                result.append(current)
            if i >= n or remain <= 0:
                return

            cand = candidates[i]
            recurse(i=i + 1, remain=remain - cand, current=(*current, cand))

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            recurse(i=i + 1, remain=remain, current=current)

        candidates.sort()
        recurse(i=0, remain=target, current=())

        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
    print(solution.combinationSum2(candidates=[1, 2, 2, 2, 5], target=5))
