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


class DetectSquares:

    def __init__(self):
        self.counter = Counter()
        self.points = []

    def add(self, point: List[int]) -> None:
        point = (point[0], point[1])
        self.counter[point] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        result = 0
        x0, y0 = point
        for (x1, y1) in self.points:
            if x0 == x1 and y0 == y1:
                continue

            distance_x = abs(x1 - x0)
            distance_y = abs(y1 - y0)

            if distance_x == distance_y:
                p1 = (x0, y1)
                p2 = (x1, y0)

                result += self.counter[p1] * self.counter[p2]

        return result


if __name__ == '__main__':
    obj = DetectSquares()
    obj.add([3, 10])
    obj.add([11, 2])
    obj.add([3, 2])
    obj.add([11, 10])
    print(obj.count(point=[11, 10]))
    print(obj.count(point=[14, 8]))
    obj.add([11, 2])
    print(obj.count(point=[11, 10]))
