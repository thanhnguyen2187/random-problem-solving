from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        valid_length = len(s) == len(t)
        if not valid_length:
            return False

        counter = Counter()
        for char in s:
            counter[char] += 1

        for char in t:
            counter[char] -= 1

        return all(value == 0 for value in counter.values())
