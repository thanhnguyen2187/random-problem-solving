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
from heapq import (
    heappush,
    heappop,
)


class SmallestInfiniteSet:

    smallest: int
    store: Set[int]

    def __init__(self):
        self.smallest = 1
        self.store = set()

    def popSmallest(self) -> int:
        if len(self.store) > 0:
            temp = min(self.store)
            self.store.remove(temp)
        else:
            temp = self.smallest
            self.smallest += 1
        return temp

    def addBack(self, num: int) -> None:
        if num < self.smallest:
            self.store.add(num)


if __name__ == '__main__':
    solution = SmallestInfiniteSet()
