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
    cycle,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
    groupby,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
)


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_changes = [
            gas_ - cost_
            for gas_, cost_ in zip(gas, cost)
        ]
        total_gas = sum(gas_changes)
        if total_gas < 0:
            return -1
        gas_changes_accumulated = list(accumulate(gas_changes))
        min_gas_change_accumulated = min(gas_changes_accumulated)
        return gas_changes_accumulated.index(min_gas_change_accumulated) + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit(gas=[2], cost=[2]))
    # print(solution.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    # print(solution.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
    # print(solution.canCompleteCircuit(gas=[5, 8, 2, 8], cost=[6, 5, 6, 6]))
