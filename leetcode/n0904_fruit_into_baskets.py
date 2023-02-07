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
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counters = [
            {fruits[0]: 1},
        ]
        for index, fruit in enumerate(fruits[1:], start=1):
            last_counter = counters[-1]
            if fruit in last_counter:
                last_counter[fruit] += 1
            elif len(last_counter) == 2:
                last_key = fruits[index - 1]
                new_counter = {
                    last_key: last_counter[last_key],
                    fruit: 1,
                }
                counters.append(new_counter)
            else:
                last_counter[fruit] = 1
        results = [
            sum(counter.values())
            for counter in counters
        ]
        return max(results)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.totalFruit(fruits=[1, 2, 1]))
    # print(solution.totalFruit(fruits=[0, 1, 2, 2]))
    # print(solution.totalFruit(fruits=[1, 2, 3, 2, 2]))
    print(solution.totalFruit(fruits=[1, 0, 1, 4, 1, 4, 1, 2, 3]))
