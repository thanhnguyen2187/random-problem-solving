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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([0])
        l, r = 0, k
        for i in range(1, r):
            while len(dq) > 0 and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        result = []
        while r < len(nums):
            result.append(nums[dq[0]])
            if dq[0] == l:
                dq.popleft()

            while len(dq) > 0 and nums[r] > nums[dq[-1]]:
                dq.pop()

            dq.append(r)

            l += 1
            r += 1

        result.append(nums[dq[0]])

        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(solution.maxSlidingWindow(nums=[1, 3, 1, 2, 0, 5], k=3))
