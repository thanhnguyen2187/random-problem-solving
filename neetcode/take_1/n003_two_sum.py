from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {
            nums[i]: i
            for i in range(0, len(nums))
        }

        for i in range(0, len(nums)):
            aux = target - nums[i]
            if aux in cache and cache[aux] != i:
                return [i, cache[aux]]


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 4, 2]
    target = 6
    result = s.twoSum(nums=nums, target=target)
    print(result)
