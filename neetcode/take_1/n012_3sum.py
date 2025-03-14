from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(0, len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif total < 0:
                    j += 1
                elif total > 0:
                    k -= 1

        return [
            list(sublist)
            for sublist in result
        ]


if __name__ == "__main__":
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    result = s.threeSum(nums=nums)
    print(result)
