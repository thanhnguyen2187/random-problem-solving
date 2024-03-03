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
    def leastInterval(self, tasks: List[str], cooling: int) -> int:
        counter = Counter()
        task_priority_queue = []
        heapq.heapify(task_priority_queue)

        for task in tasks:
            priority = counter[task] + len(task_priority_queue)
            heapq.heappush(task_priority_queue, (priority, task))
            counter[task] += 1

        result = []
        time = 0
        state = defaultdict(lambda: -101)
        backup = []

        while True:
            if len(task_priority_queue) == 0:
                break

            while len(task_priority_queue) > 0:
                priority, task = heapq.heappop(task_priority_queue)
                last_executed = state[task]
                if time - last_executed > cooling:
                    state[task] = time
                    result.append((task, time))
                    break
                else:
                    backup.append((priority + 1, task))

            for priority, task in backup:
                task_priority_queue.append((priority, task))
            backup.clear()

            time += 1

        _, last_time = result[-1]

        return last_time + 1


if __name__ == '__main__':
    solution = Solution()
    # print(solution.leastInterval(
    #     tasks=["A", "A", "A", "B", "B", "B"],
    #     cooling=2,
    # ))
    # print(solution.leastInterval(
    #     tasks=["A", "C", "A", "B", "D", "B"],
    #     cooling=1,
    # ))
    # print(solution.leastInterval(
    #     tasks=["A", "A", "A", "B", "B", "B"],
    #     cooling=3,
    # ))
    print(solution.leastInterval(
        tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
        cooling=1,
    ))
