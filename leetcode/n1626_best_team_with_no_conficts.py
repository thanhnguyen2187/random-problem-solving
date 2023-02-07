from typing import (
    DefaultDict,
    Dict,
    Iterator,
    List,
    NamedTuple,
    Optional,
    Set,
    Union,
)
from bisect import (
    bisect_left,
    bisect_right,
)
from itertools import (
    accumulate,
    chain,
    combinations,
    cycle,
    islice,
    permutations,
    product,
    repeat,
    takewhile,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score_pairs = sorted([
            (age, score)
            for age, score in zip(ages, scores)
        ])
        n = len(scores)
        results = list(map(lambda pair: pair[1], age_score_pairs))
        for index_1, index_2 in combinations(range(n), 2):
            age_1, score_1 = age_score_pairs[index_1]
            age_2, score_2 = age_score_pairs[index_2]
            if score_1 <= score_2:
                results[index_2] = max(
                    results[index_2],
                    results[index_1] + score_2,
                )

        return max(results)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.bestTeamScore(
    #     scores=[1, 3, 5, 10, 15],
    #     ages=[1, 2, 3, 4, 5],
    # ))
    print(solution.bestTeamScore(
        scores=[4, 5, 6, 5],
        ages=[2, 1, 2, 1],
    ))
