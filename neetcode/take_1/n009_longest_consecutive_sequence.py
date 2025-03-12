from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_ = 0
        for num in nums:
            if num - 1 in nums_set:
                continue

            current = 1
            while num + 1 in nums_set:
                current += 1
                num += 1

            max_ = max(max_, current)

        return max_


if __name__ == "__main__":
    s = Solution()
    nums = [2, 20, 4, 10, 3, 4, 5]
    result = s.longestConsecutive(nums=nums)
    print(result)
