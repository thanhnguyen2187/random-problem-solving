from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = sum(
            1
            for num in nums if num == 0
        )
        total_product = math.prod(
            num
            for num in nums if num != 0
        )

        if zero_count == 0:
            return [
                total_product // num
                for num in nums
            ]
        elif zero_count == 1:
            return [
                0 if num != 0 else total_product
                for num in nums
            ]
        elif zero_count > 1:
            return [
                0
                for _ in nums
            ]

        raise Exception("unreachable code")


if __name__ == "__main__":
    s = Solution()
    nums = []
    result = s.productExceptSelf(nums=nums)
    print(result)
