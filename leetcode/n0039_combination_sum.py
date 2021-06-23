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
        if remains == 0:
            results.append(accumulated.copy())
        elif remains < 0:
            return
        else:
            for index in range(start, len(candidates)):
                accumulated.append(candidates[index])
                self.attempt(
                    candidates=candidates,
                    remains=remains - candidates[index],
                    start=index,
                    accumulated=accumulated,
                    results=results
                )
                accumulated.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
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
    results = solution.combinationSum(
        candidates=[2, 3, 6, 7],
        target=7,
    )
    print(results)
