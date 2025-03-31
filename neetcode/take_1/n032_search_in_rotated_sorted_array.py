from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    # nums = [0, 1, 2, 3, 4, 5, 6]
    # nums = [6, 0, 1, 2, 3, 4, 5]
    nums = [6, 5, 0, 1, 2, 3, 4]
    target = 1.5
    result = solution.search(nums=nums, target=target)
    print(result)
