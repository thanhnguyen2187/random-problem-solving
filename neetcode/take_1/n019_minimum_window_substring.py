from collections import Counter
from typing import List


def is_substring(s_counter: Counter, t_counter: Counter):
    return all(
        s_counter[key] >= t_counter[key]
        for key in t_counter
    )


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)

        if not is_substring(s_counter=s_counter, t_counter=t_counter):
            return ""

        result = s
        s_counter.clear()
        left, right = 0, 0

        while right < len(s):
            while not is_substring(s_counter=s_counter, t_counter=t_counter) and right < len(s):
                char = s[right]
                s_counter[char] += 1
                right += 1
            while is_substring(s_counter=s_counter, t_counter=t_counter):
                result = min(result, s[left:right], key=len)
                char = s[left]
                s_counter[char] -= 1
                left += 1

        return result


if __name__ == "__main__":
    s = Solution()
    # s_ = "ADOBECODEBANCBLANCA"
    # t = "ABC"
    s_ = "ABCXAYZZYABXY"
    t = "XYZ"
    result = s.minWindow(s=s_, t=t)
    print(result)
