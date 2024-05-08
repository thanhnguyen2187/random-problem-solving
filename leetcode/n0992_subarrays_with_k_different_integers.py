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


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def at_most(k: int) -> int:
            result = 0
            l, r = 0, 0
            counter = Counter()
            while r < n:
                counter[nums[r]] += 1
                while len(counter) > k:
                    counter[nums[l]] -= 1
                    if counter[nums[l]] == 0:
                        counter.pop(nums[l])
                    l += 1
                result += r - l + 1
                r += 1
            return result

        return at_most(k=k) - at_most(k=k - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))
    print(solution.subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3))
