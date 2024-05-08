import heapq

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
    cache,
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter()
        for task in tasks:
            counter[task] += 1

        pq = []
        heapq.heapify(pq)
        for task, count in counter.items():
            heapq.heappush(pq, (-count, task))

        result = 0
        while len(pq) > 0:
            remaining = n + 1
            backup = []
            while remaining > 0:
                if len(pq) > 0:
                    count, item = heapq.heappop(pq)
                    count = -count
                    count -= 1
                    if count != 0:
                        backup.append((-count, item))
                result += 1
                if len(pq) == 0 and len(backup) == 0:
                    break
                remaining -= 1

            for pair in backup:
                heapq.heappush(pq, pair)

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.leastInterval(tasks=[0, 0, 0, 1, 1, 1], n=2))
    print(solution.leastInterval(tasks=["A", "C", "A", "B", "D", "B"], n=1))
