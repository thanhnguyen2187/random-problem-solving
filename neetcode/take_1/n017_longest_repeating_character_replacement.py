from typing import List
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        left, right, n = -1, 0, len(s)
        max_length = 0

        while right < n:
            counter[s[right]] += 1
            while right - left - max(counter.values()) > k:
                left += 1
                counter[s[left]] -= 1
            max_length = max(right - left, max_length)
            right += 1

        return max_length


if __name__ == "__main__":
    s = Solution()
    # s_ = "AAABABB"
    # k = 1
    # s_ = "ABAA"
    # k = 0
    # s_ = "XYYX"
    # k = 2
    result = s.characterReplacement(s=s_, k=k)
    print(result)
