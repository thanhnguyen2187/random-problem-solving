from typing import (
    NamedTuple,
    List,
)


class Number(NamedTuple):
    value: int
    index: int


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        indexed_numbers = dict()
        for index, number in enumerate(nums):
            if number not in indexed_numbers:
                indexed_numbers[number] = index
        indexed_numbers = sorted(indexed_numbers)

        LIS = [
            1
            for _ in range(len(indexed_numbers))
        ]
        indices = [
            value
            for key, value in indexed_numbers.items()
        ]
        for index in range(1, len(indexed_numbers)):
            if indices[index] > indices[index - 1]:
                LIS[index] = LIS[index - 1] + 1
            else:
                LIS[index] = LIS[index - 1]

        return max(LIS)


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18])
    )
    print(
        solution.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3])
    )
    print(
        solution.lengthOfLIS(nums=[7, 7, 7, 7, 7, 7, 7])
    )

