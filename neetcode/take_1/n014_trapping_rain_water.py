from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        heights_max_ltr = [heights[0]]
        heights_max_rtl = [heights[-1]]

        for h in heights[1:]:
            heights_max_ltr.append(max(heights_max_ltr[-1], h))
        for h in reversed(heights[:-1]):
            heights_max_rtl.append(max(heights_max_rtl[-1], h))
        heights_max_rtl.reverse()

        total_water = 0
        for i in range(1, len(heights) - 1):
            possible_height = min(heights_max_ltr[i - 1], heights_max_rtl[i + 1])
            total_water += max(0, possible_height - heights[i])

        return total_water


if __name__ == "__main__":
    s = Solution()
    # heights = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    heights = [4, 2, 0, 3, 2, 5]
    result = s.trap(heights=heights)
    print(result)
