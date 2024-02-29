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

        def recurse(i: int, elements: tuple, remain: int):
            if i >= len(candidates):
                return

            cand = candidates[i]
            elements_new = (*elements, cand)
            remain_new = remain - cand

            if remain_new == 0:
                result.append(elements_new)
                return
            elif remain_new < 0:
                return

            j = 0
            while i + j < len(candidates):
                recurse(i=i + j, elements=elements_new, remain=remain_new)
                j += 1

        recurse(i=0, elements=(), remain=target)

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
