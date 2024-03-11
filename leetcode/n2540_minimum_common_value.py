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
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        m, n = len(nums1), len(nums2)

        while True:
            if i >= m or j >= n:
                return -1
            elif nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                raise Exception('unreachable code')


if __name__ == '__main__':
    solution = Solution()
    print(solution.getCommon(nums1=[1, 2, 3], nums2=[0, 4]))
    print(solution.getCommon(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]))
