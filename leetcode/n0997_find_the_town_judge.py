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
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = defaultdict(set)
        being_trusted = defaultdict(set)

        for relationship in trust:
            person_1, person_2 = relationship
            trusting[person_1].add(person_2)
            being_trusted[person_2].add(person_1)

        trusted_by_everyone = {
            person
            for person in range(1, n + 1)
            if len(being_trusted[person]) == n - 1
        }
        trust_no_one = {
            person
            for person in range(1, n + 1)
            if len(trusting[person]) == 0
        }
        town_judges = trusted_by_everyone.intersection(trust_no_one)
        town_judge = next(iter(town_judges), -1)
        return town_judge


if __name__ == '__main__':
    solution = Solution()
    print(solution.findJudge(n=2, trust=[[1, 2]]))
    print(solution.findJudge(n=3, trust=[[1, 3], [2, 3]]))
    print(solution.findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
