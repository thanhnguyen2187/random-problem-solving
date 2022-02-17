from typing import (
    List,
    Iterator,
)


class Solution:

    def natural_numbers(self) -> Iterator[int]:
        current = 0
        while True:
            current += 1
            yield current

    def firstMissingPositive(self, nums: List[int]) -> int:
        existed_numbers = {
            num
            for num in nums
        }

        iterator = self.natural_numbers()
        while (num := next(iterator)) in existed_numbers:
            pass

        return num


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.firstMissingPositive(nums=[1, 2, 0])
    )
    print(
        solution.firstMissingPositive(nums=[3, 4, -1, 1])
    )
    print(
        solution.firstMissingPositive(nums=[7, 8, 9, 10, 11, 12])
    )
