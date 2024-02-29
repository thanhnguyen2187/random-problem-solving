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


class Trie:

    def __init__(self):
        self.first_node = TrieNode(char='^')
        self.set_ = set()

    def insert(self, word: str) -> None:
        cursor = self.first_node
        for char in word:
            if char in cursor.next_nodes:
                cursor = cursor.next_nodes[char]
                continue

            node = TrieNode(char=char)
            cursor.add_next(node=node)
            cursor = node

        cursor.add_next(TrieNode(char='$'))

        self.set_.add(word)

    def search(self, word: str) -> bool:
        return word in self.set_

    def startsWith(self, prefix: str) -> bool:
        cursor = self.first_node
        for char in prefix:
            if char not in cursor.next_nodes:
                return False

            cursor = cursor.next_nodes[char]

        return True


if __name__ == '__main__':
    trie = Trie()
    # trie.insert("abd")
    # trie.insert("gbc")
    # print(trie.startsWith(prefix="abc"))
    trie.insert("ab")
    print(trie.search("abc"))
    print(trie.search("ab"))
    print(trie.startsWith("abc"))
    print(trie.startsWith("ab"))
    trie.insert("ab")
