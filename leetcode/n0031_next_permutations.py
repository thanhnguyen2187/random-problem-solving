from typing import (
    List,
)
from itertools import (
    permutations,
)


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:

        index = len(nums) - 1
        temp_nums = [-1]
        while index >= 0:
            if temp_nums[-1] <= nums[index]:
                temp_nums.append(nums[index])
                nums.pop()
            else:
                nearest_index = next(
                    (  # iterator
                        nearest_index
                        for nearest_index in range(len(temp_nums))
                        if temp_nums[nearest_index] > nums[index]
                    ),
                    0,  # default
                )
                nums[index], temp_nums[nearest_index] = temp_nums[nearest_index], nums[index]
                break
            index -= 1

        nums.extend(temp_nums[1:])

        return nums


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.nextPermutation(nums=[1, 2, 3])
    )
    print(
        solution.nextPermutation(nums=[3, 2, 1])
    )
    print(
        solution.nextPermutation(nums=[1, 1, 5])
    )
    print(
        solution.nextPermutation(nums=[1, 5, 1])
    )
    print(
        solution.nextPermutation(nums=[1])
    )
