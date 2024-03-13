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
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        cars = [
            (position, speed)
            for position, speed in zip(positions, speeds)
        ]
        cars.sort(reverse=True)

        stack = [cars[0]]
        for position, speed in cars[1:]:
            arrival = (target - position) / speed
            top_position, top_speed = stack[-1]
            top_arrival = (target - top_position) / top_speed

            if arrival <= top_arrival:
                slower_car = (
                    (position, speed)
                    if speed < top_speed
                    else (top_position, top_speed)
                )
                stack[-1] = slower_car
            else:
                stack.append((position, speed))

        return len(stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.carFleet(
        target=12,
        positions=[10, 8, 0, 5, 3],
        speeds=[2, 4, 1, 1, 3],
    ))
    print(solution.carFleet(
        target=10,
        positions=[3],
        speeds=[3],
    ))
    print(solution.carFleet(
        target=100,
        positions=[0, 2, 4],
        speeds=[4, 2, 1],
    ))
