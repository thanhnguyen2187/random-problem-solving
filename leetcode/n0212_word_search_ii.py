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
    def __init__(self, char):
        self.char = char
        self.next_nodes = {}

    def add_next(self, node: 'TrieNode'):
        self.next_nodes[node.char] = node


class Solution:

    def __init__(self):
        self.start_node = TrieNode(char='^')
        self.stop_node = TrieNode(char='$')

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

            node.add_next(node=self.stop_node)

        m = len(board)
        n = len(board[0])
        result = []
        visited = set()
        def recurse(i: int, j: int, node: TrieNode, word: str):
            if not (0 <= i < m) or not (0 <= j < n):
                return
            if (i, j) in visited:
                return

            visited.add((i, j))
            char = board[i][j]
            if char not in node.next_nodes:
                visited.remove((i, j))
                return

            next_node = node.next_nodes[char]
            if '$' in node.next_nodes:
                result.append(word + char)
            next_positions = [
                (i, j + 1),
                (i, j - 1),
                (i + 1, j),
                (i - 1, j),
            ]
            for k, l in next_positions:
                recurse(i=k, j=l, node=next_node, word=word + char)

            visited.remove((i, j))

        for i, j in product(range(m), range(n)):
            visited.clear()
            recurse(i=i, j=j, node=self.start_node, word="")

        return result



if __name__ == '__main__':
    solution = Solution()
    # print(solution.findWords(
    #     board=[
    #         ["o", "a", "a", "n"],
    #         ["e", "t", "a", "e"],
    #         ["i", "h", "k", "r"],
    #         ["i", "f", "l", "v"],
    #     ],
    #     words=["oath", "pea", "eat", "rain", "oao", "oaan"],
    # ))
    # print(solution.findWords(
    #     board=[["a"]],
    #     words=["a"],
    # ))
    print(solution.findWords(
        board=[["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]],
        words=["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"],
    ))
