from typing import (
    List,
    Iterator,
)


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        row_count = len(mat)
        column_count = len(mat[0])

        if row_count * column_count != r * c:
            return mat

        def generate_matrix_iterator() -> Iterator[int]:
            row_index = 0
            column_index = 0

            while row_index < row_count:
                yield mat[row_index][column_index]
                column_index += 1
                if column_index == column_count:
                    column_index = 0
                    row_index += 1

            yield StopIteration

        iterator = generate_matrix_iterator()

        return [
            [
                next(iterator)
                for _ in range(c)
            ]
            for _ in range(r)
        ]


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.matrixReshape(
            mat=[
                [1, 2],
                [3, 4],
            ],
            r=1, c=4,
        )
    )
print(
    solution.matrixReshape(
        mat=[
            [1, 2],
            [3, 4],
        ],
        r=2, c=4,
    )
)
