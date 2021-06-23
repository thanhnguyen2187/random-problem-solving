from typing import (
    List,
)


class Solution:

    def canJump(
        self,
        nums: List[int],
    ) -> bool:

        max_index = 0

        for index, num in enumerate(nums):
            if index <= max_index:
                max_index = max(max_index, index + num)

        return max_index >= len(nums) - 1


if __name__ == "__main__":
    solution = Solution()
    # print(
    #     solution.canJump(nums=[2, 3, 1, 1, 4])
    # )
    # print(
    #     solution.canJump(nums=[3, 2, 1, 0, 4])
    # )
    # print(
    #     solution.canJump(nums=[2, 5, 0, 0])
    # )
    # print(
    #     solution.canJump(nums=[0, 2, 3])
    # )
    print(
        solution.canJump(nums=[2, 0, 0])
    )
