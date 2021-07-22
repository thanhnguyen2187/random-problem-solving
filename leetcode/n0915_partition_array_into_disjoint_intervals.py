from typing import (
    List,
    Callable,
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
from functools import (
    reduce,
)


class Solution:
    def partitionDisjoint(
        self,
        nums: List[int],
    ) -> int:

        def _append(
            sequence: List[int],
            num: int,
            comparison_function: Callable
        ) -> List[int]:
            sequence.append(
                comparison_function(
                    sequence[-1],
                    num,
                )
            )
            return sequence

        maximals = (
            reduce(
                lambda sequence, num: _append(sequence, num, max),
                nums[1:],
                [nums[0]],
            )
        )
        minimals = list(reversed(
            reduce(
                lambda sequence, num: _append(sequence, num, min),
                reversed(nums[:-1]),
                [nums[-1]],
            )
        ))

        return next(
            index + 1
            for index in range(len(nums) - 1)
            if maximals[index] <= minimals[index + 1]
        )


if __name__ == '__main__':
    solution = Solution()
    for nums in [
        [5, 0, 3, 8, 6],
        [1, 1, 1, 0, 6, 12],
    ]:
        print(solution.partitionDisjoint(nums=nums))
