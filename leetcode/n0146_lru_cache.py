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
from heapq import (
    heapify,
    heappush,
    heappop,
)


class Node:
    def __init__(
        self,
        key: int,
        value: int,
        prev: Optional['Node'] = None,
        next_: Optional['Node'] = None,
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next_


class LRUCache:

    def __init__(self, capacity: int):
        self.dict_ = {}
        self.capacity = capacity
        self.first = None
        self.last = None

    def _append(self, key: int, value: int):
        node = Node(key=key, value=value)
        self.dict_[key] = node
        if self.first is None:
            self.first = node
            self.last = node
            return

        self.last.next = node
        node.prev = self.last
        self.last = node

        if len(self.dict_) > self.capacity:
            self._pop(self.first.key)

    def _pop(self, key: int):
        node: Node = self.dict_.get(key)
        if node is None:
            return

        if len(self.dict_) == 1:
            self.first = None
            self.last = None
            self.dict_.pop(key)
            del node
            return

        if self.first is node:
            node.next.prev = None
            self.first = node.next
            self.dict_.pop(key)
            del node
            return

        if self.last is node:
            node.prev.next = None
            self.last = node.prev
            self.dict_.pop(key)
            del node
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        self.dict_.pop(key)
        del node

    def get(self, key: int) -> int:
        node: Node = self.dict_.get(key)
        if node is None:
            return -1

        self._pop(key=key)
        self._append(key=key, value=node.value)

        return node.value

    def put(self, key: int, value: int) -> None:
        self._pop(key=key)
        self._append(key=key, value=value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    lru_cache = LRUCache(capacity=2)
    lru_cache.put(key=1, value=1)
    lru_cache.put(key=2, value=2)
    print(lru_cache.get(key=1))
    lru_cache.put(key=3, value=3)
    print(lru_cache.get(key=2))
    lru_cache.put(key=4, value=4)
    print(lru_cache.get(key=1))
    print(lru_cache.get(key=3))
    print(lru_cache.get(key=4))
