from typing import (
    List,
)


class Solution:

    def attempt(
        self,
        index: int,
        nums: List[int],
        temp: List[int],
        results: List[List[int]],
    ):
        if index >= len(nums):
            results.append(
                temp.copy()
            )
            return

        temp.append(nums[index])
        self.attempt(
            index=index + 1,
            nums=nums,
            temp=temp,
            results=results,
        )
        temp.pop()
        self.attempt(
            index=index + 1,
            nums=nums,
            temp=temp,
            results=results,
        )

    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.attempt(
            index=0,
            nums=nums,
            temp=[],
            results=results,
        )
        return results


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.subsets(nums=[1, 2, 3])
    )
