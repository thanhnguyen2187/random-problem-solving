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
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        total = 0
        result = 0
        while i < n:
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                result = i + 1

            i += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit(
        gas=[1, 2, 3, 4, 5],
        cost=[3, 4, 5, 1, 2],
    ))
    print(solution.canCompleteCircuit(
        gas=[5, 8, 2, 8],
        cost=[6, 5, 6, 6],
    ))
