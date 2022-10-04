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
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population_by_year = Counter()
        for log in logs:
            for runner in range(log[0], log[1]):
                population_by_year[runner] += 1
        return max(
            sorted(population_by_year.keys()),
            key=lambda key: population_by_year[key],
        )


if __name__ == '__main__':
    solution = Solution()
