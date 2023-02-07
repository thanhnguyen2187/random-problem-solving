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
    def minFlipsMonoIncr(self, s: str) -> int:
        counter_left = Counter()
        counter_right = Counter(s)
        min_flips = []
        for character in s:
            counter_left[character] += 1
            counter_right[character] -= 1
            min_flips.append(min(
                counter_left['1'] + counter_right['0'],
                counter_left['0'] + counter_right['0'],
                counter_left['1'] + counter_right['1'],
            ))

        return min(min_flips, default=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minFlipsMonoIncr(s="00110"))
    print(solution.minFlipsMonoIncr(s="010110"))
    print(solution.minFlipsMonoIncr(s="00011000"))
    print(solution.minFlipsMonoIncr(s="11111"))
    print(solution.minFlipsMonoIncr(s="10011111110010111011"))
    print(solution.minFlipsMonoIncr(s="1111001110"))
