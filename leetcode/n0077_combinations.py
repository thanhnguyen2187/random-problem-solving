from typing import (
    List,
)


class Solution:

    def attempt(
        self,
        start: int,
        n: int,
        k: int,
        temp: List[int],
        results: List[List[int]],
    ):
        if len(temp) == k:
            results.append(
                temp.copy(),
            )
        for index in range(start, n + 1):
            temp.append(index)
            self.attempt(
                start=index + 1,
                n=n,
                k=k,
                temp=temp,
                results=results,
            )
            temp.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        self.attempt(
            start=1,
            n=n,
            k=k,
            temp=[],
            results=results,
        )
        return results


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.combine(
            n=4,
            k=2,
        )
    )
