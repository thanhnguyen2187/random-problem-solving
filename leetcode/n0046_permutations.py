from typing import (
    List,
)
from itertools import (
    permutations,
)


class Solution:

    def permute(
        self,
        nums: List[int],
    ) -> List[List[int]]:
        return [
            list(permutation)
            for permutation in permutations(nums)
        ]


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.permutate([1, 2, 3])
    )
    print(
        solution.permutate([0, 1])
    )
    print(
        solution.permutate([1])
    )
