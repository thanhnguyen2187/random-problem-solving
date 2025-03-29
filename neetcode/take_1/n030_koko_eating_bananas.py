import math
from typing import List


def sum_hours(piles: List[int], s: int):
    return sum(
        math.ceil(pile / s)
        for pile in piles
    )


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pile_max = max(piles)

        left, right = 1, pile_max
        k_min = pile_max
        while left <= right:
            mid = (left + right) // 2
            m = sum_hours(piles=piles, s=mid)
            if m <= h:
                k_min = min(mid, k_min)
                right = mid - 1
            else:
                left = mid + 1

        return k_min


if __name__ == "__main__":
    solution = Solution()
    # piles = [1, 4, 3, 2]
    # h = 9
    piles = [25, 10, 23, 4]
    h = 4
    result = solution.minEatingSpeed(piles=piles, h=h)
    print(result)
