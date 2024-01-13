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
    insort,
    bisect,
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
from heapq import (
    heappush
)


class MinStack:

    _stack: List[int]
    _stack_desc: List[int]

    def __init__(self):
        self._stack = []
        self._stack_desc = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if (
            len(self._stack_desc) == 0 or
            val <= self._stack_desc[-1]
        ):
            self._stack_desc.append(val)

    def pop(self) -> None:
        top = self._stack.pop()
        if self._stack_desc[-1] == top:
            self._stack_desc.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._stack_desc[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == '__main__':
    solution = Solution()
