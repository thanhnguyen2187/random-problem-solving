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
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {
            character: index
            for index, character in enumerate(order)
        }

        def word_to_alien_index(word: str):
            return list(map(
                lambda character: order_dict[character],
                word,
            ))

        sorted_words = sorted(
            words,
            key=word_to_alien_index,
        )
        return words == sorted_words


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAlienSorted(
        words=["hello", "leetcode"],
        order="hlabcdefgijkmnopqrstuvwxyz",
    ))
    print(solution.isAlienSorted(
        words=["word", "world", "row"],
        order="worldabcefghijkmnpqstuvxyz",
    ))
    print(solution.isAlienSorted(
        words=["apple", "app"],
        order="abcdefghijklmnopqrstuvwxyz",
    ))
