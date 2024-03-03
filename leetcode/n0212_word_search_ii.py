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

    def add_next(self, node: 'TrieNode'):
        self.next_nodes[node.char] = node


class Solution:
    start_node: TrieNode
    stop_node: TrieNode

    def __init__(self):
        self.start_node = TrieNode('^')
        self.stop_node = TrieNode('$')

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            cursor = self.start_node
            for char in word:
                if char in cursor.next_nodes:
                    cursor = cursor.next_nodes[char]
                    continue

                node = TrieNode(char=char)
                cursor.add_next(node=node)
                cursor = node

            cursor.add_next(node=self.stop_node)

        result = set()
        m = len(board)
        n = len(board[0])
        def recurse(cursor: TrieNode, i: int, j: int, word: str):
            if (i, j) in visited:
                return
            if not (0 <= i < m and 0 <= j < n):
                return

            char = board[i][j]
            word = word + char
            visited.add((i, j))
            if char in cursor.next_nodes:
                cursor = cursor.next_nodes[char]
                if '$' in cursor.next_nodes:
                    result.add(word)
                for k, l in (
                    (i + 1, j),
                    (i - 1, j),
                    (i, j + 1),
                    (i, j - 1),
                ):
                    recurse(cursor=cursor, i=k, j=l, word=word)
            visited.remove((i, j))

        for i, j in product(range(m), range(n)):
            visited = set()
            recurse(cursor=self.start_node, i=i, j=j, word="")

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords(
        board=[
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        words=["oath", "pea", "eat", "rain", "oao", "oaan"],
    ))
    # print(solution.findWords(
    #     board=[["a"]],
    #     words=["a"],
    # ))
    # print(solution.findWords(
    #     board=[["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]],
    #     words=["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"],
    # ))
