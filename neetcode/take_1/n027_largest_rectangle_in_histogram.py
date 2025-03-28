from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            k = i
            while len(stack) > 0 and stack[-1][0] > h:
                top_h, j = stack.pop()
                area = (i - j) * top_h
                max_area = max(max_area, area)
                k = j
            stack.append((h, k))

        n = len(heights)
        while len(stack) > 0:
            top_h, j = stack.pop()
            area = (n - j) * top_h
            max_area = max(max_area, area)

        return max_area


if __name__ == "__main__":
    solution = Solution()
    heights = [2, 1, 4, 3, 4, 3, 7, 2, 1]
    result = solution.largestRectangleArea(heights=heights)
    print(result)
