from typing import (
    List,
)


class Solution:

    def trap(self, heights: List[int]) -> int:

        if len(heights) < 3:
            return 0

        left_index = 0
        right_index = len(heights) - 1
        left_max = heights[left_index]
        right_max = heights[right_index]
        total = 0

        while left_index <= right_index:
            left_height = heights[left_index]
            right_height = heights[right_index]
            if left_height < right_height:
                if left_height < left_max:
                    total += left_max - left_height
                else:
                    left_max = left_height
                left_index += 1
            else:
                if right_height < right_max:
                    total += right_max - right_height
                else:
                    right_max = right_height
                right_index -= 1

        return total


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.trap(heights=[
            0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1,
        ])
    )