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


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        people = sorted(people)
        left_index = 0
        right_index = len(people) - 1
        while left_index <= right_index:
            if people[left_index] + people[right_index] <= limit:
                result += 1
                left_index += 1
                right_index -= 1
            else:
                result += 1
                right_index -= 1
        return result

if __name__ == '__main__':
    solution = Solution()
