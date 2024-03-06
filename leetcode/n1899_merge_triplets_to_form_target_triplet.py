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
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1, t2, t3 = target
        triplets = [
            (i, j, k)
            for i, j, k in triplets
            if (
                i <= t1 and j <= t2 and k <= t3 and
                (i == t1 or j == t2 or k == t3)
            )
        ]

        target_met = [False, False, False]
        for i, j, k in triplets:
            if i == t1:
                target_met[0] = True
            if j == t2:
                target_met[1] = True
            if k == t3:
                target_met[2] = True

        return all(target_met)



if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeTriplets(
        triplets=[[3, 5, 1], [10, 5, 7]],
        target=[3, 5, 7],
    ))
