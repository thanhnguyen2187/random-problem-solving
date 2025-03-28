from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 2, 4, 6, 8]
    target = 3
    result = solution.search(nums=nums, target=target)
    print(result)
