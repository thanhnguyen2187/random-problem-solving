from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        max_left, max_right = heights[left], heights[right]

        total_water = 0
        while left < right:
            possible_water = min(max_left, max_right) - min(heights[left], heights[right])
            possible_water = max(0, possible_water)
            total_water += possible_water
            max_left = max(heights[left], max_left)
            max_right = max(heights[right], max_right)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return total_water


if __name__ == "__main__":
    s = Solution()
    heights = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    # heights = [4, 2, 0, 3, 2, 5]
    result = s.trap(heights=heights)
    print(result)
