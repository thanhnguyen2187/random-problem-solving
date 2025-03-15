from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_ = 0
        while left < right:
            min_height = min(heights[left], heights[right])
            distance = right - left
            max_ = max(
                max_,
                min_height * distance,
            )
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_


if __name__ == "__main__":
    s = Solution()
    heights = [1, 7, 2, 5, 4, 7, 3, 6]
    result = s.maxArea(heights=heights)
    print(result)
