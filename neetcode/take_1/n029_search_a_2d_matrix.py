from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, (m * n) - 1
        while left <= right:
            mid = (left + right) // 2
            i = mid // n
            j = mid - (n * i)
            x = matrix[i][j]
            if target == x:
                return True
            elif target > x:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [1, 2, 4, 8],
        [10, 11, 12, 13],
        [14, 20, 30, 40],
    ]
    target = 0
    result = solution.searchMatrix(
        matrix=matrix,
        target=target,
    )
    print(result)
