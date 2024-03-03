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
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        cached = defaultdict(set)
        for i, word in enumerate(wordList):
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                cached[pattern].add(i)
        for j in range(len(beginWord)):
            pattern = beginWord[:j] + '*' + beginWord[j + 1:]
            cached[pattern].add(-1)

        graph = defaultdict(set)
        for _, indices in cached.items():
            for i in indices:
                graph[i].update(indices)
                graph[i].remove(i)

        dq = deque([(-1, 1)])
        visited = set()
        while len(dq) > 0:
            i, level = dq.popleft()
            if i in visited:
                continue
            if i != -1 and wordList[i] == endWord:
                return level

            visited.add(i)
            for j in graph[i]:
                dq.append((j, level + 1))
            graph[i].clear()

        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.ladderLength(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    ))
    print(solution.ladderLength(
        beginWord="la",
        endWord="ki",
        wordList=["li", "ki", "km", "am"],
    ))
