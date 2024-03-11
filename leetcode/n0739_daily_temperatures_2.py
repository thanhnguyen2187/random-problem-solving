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
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = list(repeat(0, n))
        for i in range(0, n):
            temperature = temperatures[i]
            while len(stack) > 0:
                top, j = stack[-1]
                if top < temperature:
                    stack.pop()
                    result[j] = i - j
                else:
                    break

            stack.append((temperature, i))

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
    print(solution.dailyTemperatures(temperatures=[30, 40, 50, 60]))
    print(solution.dailyTemperatures(temperatures=[30, 60, 90]))
