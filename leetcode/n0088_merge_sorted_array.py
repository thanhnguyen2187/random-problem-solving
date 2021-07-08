from typing import (
    List,
)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n > 0:
            nums1[-n:] = nums2
        nums1.sort()
        # print(nums1)


if __name__ == "__main__":
    solution = Solution()
    solution.merge(
        nums1=[1, 2, 3, 0, 0, 0],
        nums2=[2, 5, 6],
        m=3,
        n=3,
    )
    solution.merge(
        nums1=[1],
        nums2=[],
        m=1,
        n=0,
    )
    solution.merge(
        nums1=[0],
        nums2=[1],
        m=0,
        n=1,
    )
    solution.merge(
        nums1=[-1, 0, 0, 3, 3, 3, 0, 0, 0],
        nums2=[1, 2, 2],
        m=6,
        n=3,
    )
