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


def solution(A: [int]):
    counter = Counter(A)
    values = sorted(counter.values(), reverse=True)
    table = set()
    for value in values:
        while value in table and value > 0:
            value -= 1
        table.add(value)
    table.discard(0)
    return sum(values) - sum(table)


if __name__ == '__main__':
    print(solution([5, 3, 3, 2, 5, 2, 3, 2]))
    print(solution([127, 15, 3, 8, 10]))
    print(solution([1_000_000_000, 1_000_000_000, 5, 5, 5, 2, 2, 2, 0, 0]))
