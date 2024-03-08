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
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {
            char: set()
            for word in words
            for char in word
        }
        for word_1, word_2 in zip(words, words[1:]):
            if word_2.startswith(word_1):
                return ''
            for char_1, char_2 in zip(word_1, word_2):
                if char_1 != char_2:
                    graph[char_1].add(char_2)
                    break

        permanents = set()
        temporaries = set()
        result = []
        is_cyclic = False
        def recurse(char: str):
            nonlocal is_cyclic
            if char in permanents or is_cyclic:
                return
            if char in temporaries:
                is_cyclic = True
                return

            temporaries.add(char)
            for neighbor in graph[char]:
                recurse(neighbor)
            temporaries.remove(char)

            result.append(char)
            permanents.add(char)

        for char in graph:
            if char not in permanents:
                recurse(char)

        if is_cyclic:
            return ''

        result.reverse()
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    # words = ["hrn", "hrf", "er", "enn", "rfnn"]
    words = ["aaa", "aa", "a"]
    print(solution.foreignDictionary(words=words))
