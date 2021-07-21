from typing import (
    List,
    NamedTuple,
    Union,
)
from itertools import (
    accumulate,
)
from bisect import (
    bisect_left,
    bisect_right,
    insort,
    insort_left,
)


class Node(NamedTuple):
    value: Union[int, float]
    children: List['Node']


class Solution:

    def lengthOfLIS(
        self,
        nums: List[int],
    ) -> int:

        n = len(nums)
        LIS = [
            1
            for _ in range(n)
        ]

        for first_index in range(1, n):
            for second_index in range(0, first_index):
                if nums[first_index] > nums[second_index]:
                    LIS[first_index] = max(
                        LIS[second_index] + 1,
                        LIS[first_index],
                    )

        return max(LIS)

if __name__ == '__main__':
    solution = Solution()
    print(
        solution.lengthOfLIS(
            nums=[10, 9, 2, 5, 3, 7, 101, 18],
        )
    )
    print(
        solution.lengthOfLIS(
            nums=[0, 1, 0, 3, 2, 3],
        )
    )
    print(
        solution.lengthOfLIS(
            nums=[7, 7, 7, 7, 7, 7, 7],
        )
    )
    print(
        solution.lengthOfLIS(
            nums=[7, 5, 6, 2, 1, 2, 3, 4, 5, 6, 7, 8],
        )
    )

