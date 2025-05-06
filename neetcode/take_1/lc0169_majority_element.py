from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        m = nums[0]

        for num in nums[1:]:
            if count == 0:
                m = num
                count = 1
            elif m == num:
                count += 1
            else:
                count -= 1

        return m





if __name__ == "__main__":
    solution = Solution()
    nums = []
    result = solution.solution(nums=nums)
    print(result)
