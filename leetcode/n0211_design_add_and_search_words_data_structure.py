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
    next_nodes: dict
    char: str

    def __init__(self, char: str):
        self.char = char
        self.next_nodes = {}

    def add_next(self, node: 'TrieNode'):
        self.next_nodes[node.char] = node


class WordDictionary:
    def __init__(self):
        self.first_node = TrieNode(char='^')

    def addWord(self, word: str) -> None:
        cursor = self.first_node
        for char in word:
            if char in cursor.next_nodes:
                cursor = cursor.next_nodes[char]
                continue

            node = TrieNode(char=char)
            cursor.add_next(node=node)
            cursor = node

        cursor.add_next(TrieNode(char='$'))

    def search(self, word: str) -> bool:
        dq = deque([(self.first_node, 0)])

        while len(dq) > 0:
            cursor, i = dq.pop()
            if cursor.char == '$':
                return True

            char = (
                word[i]
                if i < len(word)
                else '$'
            )
            if char in cursor.next_nodes:
                dq.append((cursor.next_nodes[char], i + 1))
            elif char == '.':
                dq.extend([
                    (next_cursor, i + 1)
                    for next_cursor in cursor.next_nodes.values()
                    if next_cursor.char != '$'
                ])

        return False



if __name__ == '__main__':
    wd = WordDictionary()
    wd.addWord(word="bad")
    wd.addWord(word="dad")
    wd.addWord(word="mad")
    wd.addWord(word="pad")
    # print(wd.search(word="bad"))
    print(wd.search(word=".ad"))
    print(wd.search(word="b.."))
    print(wd.search(word="b.b"))
    # wd.addWord(word="a")
    # wd.addWord(word="a")
    # print(wd.search(word="a."))
