from typing import (
    List,
)
from itertools import (
    combinations,
)
from bisect import (
    insort,
    bisect_left,
    bisect_right,
)


class Solution:

    def triangleNumber(
        self,
        nums: List[int],
    ) -> int:

        result = 0
        nums.sort()

        for k in range(2, len(nums)):
            i, j = 0, k - 1
            while i <= j:
                if nums[i] + nums[j] > nums[k]:
                    result += j - i
                    j -= 1
                else:
                    i += 1

        return result


if __name__ == '__main__':
    solution = Solution()

    for nums in [
        [2, 2, 3, 4],
        [4, 2, 3, 4],
    ]:
        print(
            solution.triangleNumber(
                nums=nums,
            )
        )
