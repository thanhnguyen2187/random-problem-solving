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


class TrieNode:
    char: str
    next_nodes: dict

    def __init__(self, char: str):
        self.char = char
        self.next_nodes = {}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key=len)

        @cache
        def recurse(i: int) -> bool:
            if i == len(s):
                return True
            for word in wordDict:
                if s[i:].startswith(word) and recurse(i + len(word)):
                    return True

            return False

        return recurse(i=0)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.wordBreak(s="catsanddog", wordDict=["cats","dog","sand","and","cat"]))
    print(solution.wordBreak(s="aaaaaaa", wordDict=["aaaa","aaa"]))
