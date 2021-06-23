from typing import (
    List,
)


class Solution:

    def jump(
        self,
        nums: List[int],
    ) -> int:
        tracks = [
            10 ** 4 + 1
            for _ in nums
        ]
        tracks[0] = 0

        for index in range(0, len(nums)):
            for step in range(1, nums[index] + 1):
                next_step = index + step
                if next_step < len(tracks):
                    tracks[next_step] = min(
                        tracks[next_step],
                        tracks[index] + 1,
                        )

        return tracks[-1]


if __name__ == '__main__':
    solution = Solution()

    print(
        solution.jump(nums=[2, 3, 1, 1, 4])
    )
    print(
        solution.jump(nums=[2, 3, 0, 1, 4])
    )
