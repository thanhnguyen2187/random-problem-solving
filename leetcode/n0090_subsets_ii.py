from typing import (
    List,
)


class Solution:

    def attempt(
        self,
        nums: List[int],
        start: int,
        temp: List[int],
        result: List[List[int]],
    ):
        result.append(temp.copy())
        for index in range(start, len(nums)):
            if (
                index > start and
                nums[index] == nums[index - 1]
            ):
                continue

            temp.append(nums[index])
            self.attempt(
                nums=nums,
                start=index + 1,
                temp=temp,
                result=result,
            )
            temp.pop()

    def subsetsWithDup(
        self,
        nums: List[int],
    ) -> List[List[int]]:
        result = []

        nums.sort()
        self.attempt(
            nums=nums,
            start=0,
            temp=[],
            result=result,
        )

        return result


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.subsetsWithDup(
            nums=[1, 2, 2],
        )
    )
    print(
        solution.subsetsWithDup(
            nums=[0],
        )
    )
