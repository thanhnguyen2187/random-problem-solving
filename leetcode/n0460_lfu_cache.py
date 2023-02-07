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
    OrderedDict,
)


class LFUCache:
    capacity: int
    data: dict
    frequency_to_keys: DefaultDict

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.frequency_to_keys = defaultdict(dict)

    def get(self, key: int) -> int:
        if key in self.data:
            value, frequency = self.data[key]
            self.frequency_to_keys[frequency].pop(key)
            self.data[key] = (value, frequency + 1)
            self.frequency_to_keys[frequency + 1][key] = True
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        elif key in self.data:
            _, frequency = self.data[key]
            self.frequency_to_keys[frequency].pop(key)
            self.data[key] = (value, frequency + 1)
            self.frequency_to_keys[frequency + 1][key] = True
        elif key not in self.data:
            if len(self.data) == self.capacity:
                lru_frequency, lru_key = next(
                    (frequency, key)
                    for frequency, keys in self.frequency_to_keys.items()
                    for key in keys
                )
                self.data.pop(lru_key)
                self.frequency_to_keys[lru_frequency].pop(lru_key)
            self.data[key] = (value, 1)
            self.frequency_to_keys[1][key] = True


if __name__ == '__main__':
    cache = LFUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

    cache = LFUCache(capacity=2)
    cache.put(2, 1)
    cache.put(3, 2)
    print(cache.get(3))
    print(cache.get(2))
    cache.put(4, 3)
    print(cache.get(2))
    print(cache.get(3))
    print(cache.get(4))
