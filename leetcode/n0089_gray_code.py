from typing import (
    List,
)
from itertools import (
    cycle,
)


class Solution:

    def flip(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        else:
            return [
                *self.flip(n - 1),
                2 ** (n - 1),
                *self.flip(n - 1),
            ]

    def grayCode(self, n: int) -> List[int]:

        result = [0]
        flip_bits = self.flip(n)
        for bit in flip_bits:
            result.append(
                result[-1] ^ bit
            )

        return result


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.grayCode(2)
    )
    print(
        solution.grayCode(3)
    )
    print(
        solution.grayCode(4)
    )
