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


class MinStack:

    def __init__(self):
        self.values = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.values.append(val)
        if len(self.min_values) == 0:
            self.min_values.append(val)
            return

        self.min_values.append(
            min(
                self.min_values[-1],
                val,
            )
        )

    def pop(self) -> None:
        self.values.pop()
        self.min_values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
