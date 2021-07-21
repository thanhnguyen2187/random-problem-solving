from typing import (
    List,
    Set,
    Tuple,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    product,
    accumulate,
    takewhile,
    islice,
    chain,
    cycle,
    repeat,
)


class Solution:

    def fourSum(
        self,
        nums: List[int],
        target: int,
    ) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        results: Set[Tuple[int, int, int, int]] = set()

        for index_1, index_4 in product(
            range(0, n - 3),
            range(n - 1, 2, -1),
        ):
            if (
                index_1 < index_4 and
                index_4 - index_1 > 2
            ):
                index_2 = index_1 + 1
                index_3 = index_4 - 1

                while (
                    index_2 < index_3
                    # and index_2 < index_4
                    # and index_1 < index_3
                ):
                    target_current = (
                        nums[index_1] +
                        nums[index_2] +
                        nums[index_3] +
                        nums[index_4]
                    )
                    if target_current == target:
                        results.add(
                            (
                                nums[index_1],
                                nums[index_2],
                                nums[index_3],
                                nums[index_4],
                            )
                        )
                        index_2 += 1
                        index_3 -= 1
                    elif target_current < target:
                        index_2 += 1
                    elif target_current > target:
                        index_3 -= 1

        return [
            list(result)
            for result in results
        ]


if __name__ == '__main__':
    solution = Solution()
    for nums, target in [
        ([1, 0, -1, 0, -2, 2], 0,),
        ([2, 2, 2, 2], 8,),
        ([2, 2, 2, 2, 2], 8,),
    ]:
        print(
            solution.fourSum(
                nums=nums,
                target=target,
            )
        )
