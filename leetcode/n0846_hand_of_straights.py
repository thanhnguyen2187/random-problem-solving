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
    def isNStraightHand(self, hand: List[int], n: int) -> bool:
        if n == 1:
            return True
        if len(hand) % n != 0:
            return False

        counter = Counter(hand)
        heap = list(counter.items())
        heapq.heapify(heap)

        while len(heap) > 0:
            pairs = [
                heapq.heappop(heap)
                for _ in range(n)
                if len(heap) > 0
            ]
            if len(pairs) < n:
                return False
            for pair_1, pair_2 in zip(pairs, pairs[1:]):
                if pair_1[0] + 1 != pair_2[0]:
                    return False

            pairs = [
                (card, count - 1)
                for card, count in pairs
                if count - 1 > 0
            ]
            for pair in pairs:
                heapq.heappush(heap, pair)

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isNStraightHand(hand=[1, 1, 2, 2, 3, 3], n=3))
    print(solution.isNStraightHand(hand=[0, 0], n=2))
    print(solution.isNStraightHand(hand=[3, 1, 2], n=3))
    print(solution.isNStraightHand(hand=[1,2,3,6,2,3,4,7,8], n=3))
