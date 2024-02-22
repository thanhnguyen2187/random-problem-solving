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
    def findMedianSortedArrays(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> float:

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A's index
            j = half - i - 2  # B's index

            A_left = (
                A[i]
                if i >= 0
                else float("-inf")
            )
            A_right = (
                A[i + 1]
                if i + 1 < len(A)
                else float("inf")
            )
            B_left = (
                B[j]
                if j >= 0
                else float("-inf")
            )
            B_right = (
                B[j + 1]
                if j + 1 < len(B)
                else float("inf")
            )

            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 1:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1


if __name__ == '__main__':
    solution = Solution()
