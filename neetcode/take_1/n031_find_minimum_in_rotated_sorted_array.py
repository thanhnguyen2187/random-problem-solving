from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if right - left <= 1:
                return min([nums[left], nums[right]])
            elif nums[left] <= nums[right]:
                return nums[left]
            elif nums[left] >= nums[mid]:
                right = mid
            else:
                left = mid

        raise Exception("unreachable code")


if __name__ == "__main__":
    solution = Solution()
    # nums = [1, 2, 3, 4, 5, 6]
    # nums = [2, 3, 4, 5, 6, 1]
    # nums = [3, 4, 5, 6, 1, 2]
    # nums = [4, 5, 6, 1, 2, 3]
    # nums = [5, 6, 1, 2, 3, 4]
    nums = [6, 1, 2, 3, 4, 5]
    result = solution.findMin(nums=nums)
    print(result)
