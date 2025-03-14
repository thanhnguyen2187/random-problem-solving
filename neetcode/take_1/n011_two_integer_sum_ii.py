from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            target_current = numbers[left] + numbers[right]
            if target_current == target:
                return [left + 1, right + 1]
            elif target_current > target:
                right -= 1
            elif target_current < target:
                left += 1

        raise Exception("unreachable code")


if __name__ == "__main__":
    s = Solution()
    numbers = [1, 2, 3, 4]
    target = 3
    result = s.twoSum(numbers=numbers, target=target)
    print(result)
