from typing import List


def isBadVersion(version: int) -> bool:
    return version >= 5


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        # raise Exception(f"unreachable code: left={left}, right={right}, mid={mid}")
        return left


if __name__ == "__main__":
    solution = Solution()
    nums = []
    result = solution.firstBadVersion(n=10)
    print(result)
