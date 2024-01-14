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
        result = list(repeat(0, len(temperatures)))
        stack = [0]
        for index in range(1, len(temperatures)):
            current = temperatures[index]
            while len(stack) > 0:
                top_index = stack[-1]
                top = temperatures[top_index]
                if top < current:
                    stack.pop()
                    result[top_index] = index - top_index
                else:
                    break
            stack.append(index)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
    print(solution.dailyTemperatures(temperatures=[30, 40, 50, 60]))
    print(solution.dailyTemperatures(temperatures=[30, 60, 90]))
