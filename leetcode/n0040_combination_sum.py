from typing import (
    List,
)
from itertools import (
    product,
)

class Solution:

    def attempt(
        self,
        candidates: List[int],
        start: int,
        remains: int,
        accumulated: List[int],
        results: List[List[int]],
    ) -> None:
        if remains < 0:
            return
        elif remains == 0:
            results.append(accumulated.copy())
        else:
            for index in range(start, len(candidates)):
                if (
                    index > start and
                    candidates[index] == candidates[index - 1]
                ):
                    continue

                accumulated.append(candidates[index])
                self.attempt(
                    candidates=candidates,
                    remains=remains - candidates[index],
                    start=index + 1,
                    accumulated=accumulated,
                    results=results,
                )
                accumulated.pop()


    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        self.attempt(
            candidates=candidates,
            start=0,
            remains=target,
            accumulated=[],
            results=results,
        )
        return results


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.combinationSum2(
            candidates=[2, 5, 2, 1, 2],
            target=5,
        )
    )
    print(
        solution.combinationSum2(
            candidates=[10, 1, 2, 7, 6, 1, 5],
            target=8,
        )
    )
