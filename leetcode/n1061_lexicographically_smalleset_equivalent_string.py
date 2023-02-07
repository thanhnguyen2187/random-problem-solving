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
    groupby,
)
from functools import (
    cached_property,
)
from collections import (
    defaultdict,
    deque,
    Counter,
)


class DisjointSet:
    tracker: DefaultDict

    def find(self, *items) -> bool:
        return all([
            self.tracker[item_1] == self.tracker[item_2]
            for item_1, item_2 in zip(items, items[1:])
        ])

    def union(self, *items) -> bool:
        indexes = {
            self.tracker[item]
            for item in items
        }
        min_index = min(indexes)
        for item in self.tracker.keys():
            if self.tracker[item] in indexes:
                self.tracker[item] = min_index

    def __init__(self):
        self.tracker = defaultdict(lambda: len(self.tracker))


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        disjoint_set = DisjointSet()

        for character_1, character_2 in zip(s1, s2):
            disjoint_set.union(character_1, character_2)

        groups = defaultdict(set)
        for character, index in disjoint_set.tracker.items():
            groups[index].add(character)

        def find_min_character_in_groups(character: str):
            for group in groups.values():
                if character in group:
                    return min(group)

            return character

        result = ''.join(
            find_min_character_in_groups(character)
            for character in baseStr
        )

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.smallestEquivalentString(s1="parker", s2="morris", baseStr="parser"))
    print(solution.smallestEquivalentString(s1="hello", s2="world", baseStr="hold"))
    print(solution.smallestEquivalentString(s1="leetcode", s2="programs", baseStr="sourcecode"))
