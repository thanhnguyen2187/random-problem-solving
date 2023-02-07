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


# noinspection PyShadowingNames
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)

        def dp(word: str):
            result = [
                True,
                *repeat(False, len(word)),
            ]
            for index in range(1, len(word)):
                result[index] = any(
                    result[index_2] and word[index_2:index] in words_set
                    for index_2 in range(index)
                )
            result[len(word)] = any(
                result[index_2] and word[index_2:] in words_set
                for index_2 in range(1, len(word))
            )
            return result[-1]

        return [
            word
            for word in words
            if dp(word=word)
        ]


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.findAllConcatenatedWordsInADict(
            words=["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"],
        )
    )
