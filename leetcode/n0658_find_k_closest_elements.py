import math
from typing import (
    List,
)
from bisect import (
    bisect_left,
)
from itertools import (
    cycle,
    count,
)
from collections import (
    deque,
)


class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        distances = [
            (
                abs(x - a),
                index
            )
            for index, a in enumerate(arr)
        ]
        # distances.sort(reverse=True)
        distances.sort()

        return sorted([
            arr[index]
            for _, index in distances[0:k]
        ])


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.findClosestElements(
            arr=[1, 2, 3, 4, 5],
            k=4,
            x=3,
        )
    )
    print(
        solution.findClosestElements(
            arr=[1, 2, 3, 4, 5],
            k=4,
            x=-1,
        )
    )
    print(
        solution.findClosestElements(
            arr=[0, 1, 1, 1, 2, 3, 6, 7, 8, 9],
            k=9,
            x=4,
        )
    )
    print(
        solution.findClosestElements(
            arr=[0, 0, 1, 2, 3, 3, 4, 7, 7, 8],
            k=3,
            x=5,
        )  # 3 3 4
    )
