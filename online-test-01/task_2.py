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


def solution(n):
    d = [0] * 30
    l = 0
    while n > 0:
        d[l] = n % 2
        n //= 2
        l += 1
    for p in range(l // 2 + 1, 0, -1):
        ok = True
        for i in range(l - p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1


if __name__ == '__main__':
    # n = 1_000_000_000
    # n = 900_000_300
    # n = 956
    n = 0b11001111100111
    print(solution(n))
    print(format(n, 'b'))
