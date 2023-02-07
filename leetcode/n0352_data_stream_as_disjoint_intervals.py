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
    insort,
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


class SummaryRanges:

    numbers: List[int]

    def __init__(self):
        self.numbers = []

    def addNum(self, value: int) -> None:
        insort(self.numbers, value)

    def getIntervals(self) -> List[List[int]]:
        if len(self.numbers) == 0:
            return []

        intervals: List = [
            [self.numbers[0], self.numbers[0]],
        ]
        for number in self.numbers[1:]:
            latest_interval = intervals[-1]
            low, high = latest_interval
            if high == number:
                continue
            elif high + 1 == number:
                intervals[-1] = [low, number]
            else:
                intervals.append([number, number])

        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()


if __name__ == '__main__':
    obj = SummaryRanges()
    obj.addNum(1)
    print(obj.getIntervals())

    obj.addNum(3)
    print(obj.getIntervals())

    obj.addNum(7)
    print(obj.getIntervals())

    obj.addNum(2)
    print(obj.getIntervals())

    obj.addNum(6)
    print(obj.getIntervals())
