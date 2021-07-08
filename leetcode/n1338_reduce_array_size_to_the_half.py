from collections import (
    Counter,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    accumulate,
)
from typing import (
    List,
    NamedTuple,
)


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        target = len(arr) // 2

        sorted_values = sorted(counter.values())
        ranges = [
            (begin, end)
            for begin, end in zip(
                accumulate(sorted_values),
                accumulate(reversed(sorted_values))
            )
        ]

        return next(
            (
                index
                for index, range_ in enumerate(ranges, start=1)
                if range_[0] <= target <= range_[1]
            ),
            len(ranges)
        )


if __name__ == '__main__':
    solution = Solution()
    # print(
    #     solution.minSetSize(
    #         arr=[
    #             3, 3, 3, 3,
    #             5, 5, 5,
    #             2, 2,
    #             7,
    #         ],
    #     )
    # )
    # print(
    #     solution.minSetSize(
    #         arr=[
    #             7, 7, 7, 7, 7, 7,
    #         ],
    #     )
    # )
    # print(
    #     solution.minSetSize(
    #         arr=[
    #             1, 9,
    #         ],
    #     )
    # )
    # print(
    #     solution.minSetSize(
    #         arr=[
    #             1000, 1000,
    #             3, 7
    #         ],
    #     )
    # )
    print(
        solution.minSetSize(
            arr=[
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            ],
        )
    )
