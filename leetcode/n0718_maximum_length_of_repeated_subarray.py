from typing import (
    List,
    Iterator,
)


class Solution:
    def findLength(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> int:

        max_ = 0

        for first_index in range(len(nums1)):
            possible_max = sum(
                1
                for first_number, second_number in zip(
                    nums1[first_index:],
                    nums2,
                )
                if first_number == second_number
            )
            max_ = max(max_, possible_max)

        return max_


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.findLength(
            nums1=[1, 2, 3, 2, 1],
            nums2=[3, 2, 1, 4, 7],
        )
    )
    print(
        solution.findLength(
            nums1=[0, 0, 0, 0, 0],
            nums2=[0, 0, 0, 0, 0],
        )
    )
    print(
        solution.findLength(
            nums1=[1, 0, 0, 0, 0],
            nums2=[0, 0, 0, 0, 1],
        )
    )
    print(
        solution.findLength(
            nums1=[0, 0, 0, 0, 1],
            nums2=[1, 0, 0, 0, 0],
        )
    )
