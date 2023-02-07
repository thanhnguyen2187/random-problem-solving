from math import (
    ceil,
)
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

task_number_to_round_count = {
    3: 1,
    4: 2,
    5: 2,
}


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        total_round_count = 0
        difficulty_to_task_number = Counter(tasks)
        for difficulty, task_number in difficulty_to_task_number.items():
            if task_number == 1:
                return -1
            round_count = ceil(task_number / 3)
            total_round_count += round_count
        return total_round_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
    print(solution.minimumRounds(tasks=[2, 3, 3]))
