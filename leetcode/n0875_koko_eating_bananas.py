import math

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


def calculate_hours(piles: List[int], speed: int) -> int:
    return sum(
        math.ceil(pile / speed)
        for pile in piles
    )


class Solution:
    def minEatingSpeed(self, piles: List[int], target_hour: int) -> int:
        speed_left = 1
        speed_right = max(piles)
        speed_minimum = speed_right

        while speed_left <= speed_right:
            speed_middle = (speed_left + speed_right) // 2
            hour_middle = calculate_hours(piles=piles, speed=speed_middle)

            if hour_middle <= target_hour:
                speed_minimum = min(speed_minimum, speed_middle)
                speed_right = speed_middle - 1
            else:
                speed_left = speed_middle + 1

        return speed_minimum


if __name__ == '__main__':
    solution = Solution()
    # piles = [3, 6, 7, 11]
    # target_hour = 8
    # piles = [30, 11, 23, 4, 20]
    # target_hour = 5
    piles = [30, 11, 23, 4, 20]
    target_hour = 6
    print(solution.minEatingSpeed(piles=piles, target_hour=target_hour))
