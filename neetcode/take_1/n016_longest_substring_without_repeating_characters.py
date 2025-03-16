from typing import List
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        match len(s):
            case 0:
                return 0
            case 1:
                return 1

        left, right, n = 0, 0, len(s)
        counter =  Counter()

        max_length = 0
        while right < n:
            char = s[right]
            counter[char] += 1
            while counter[char] > 1:
                counter[s[left]] -= 1
                left += 1
            right += 1
            max_length = max(max_length, right - left)

        return max_length


if __name__ == "__main__":
    s = Solution()
    # s_ = "abcabcbb"
    # s_ = "pwwkew"
    s_ = "au"
    result = s.lengthOfLongestSubstring(s=s_)
    print(result)
