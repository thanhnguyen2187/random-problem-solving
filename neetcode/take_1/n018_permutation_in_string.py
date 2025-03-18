from typing import List
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        s1_counter = Counter(s1[:n])
        s2_counter = Counter(s2[:n - 1])

        i, j = 0, n - 1
        while j < m:
            char = s2[j]
            s2_counter[char] += 1
            if all(
                s1_counter[key] == s2_counter[key]
                for key in s1_counter
            ):
                return True
            char = s2[i]
            s2_counter[char] -= 1
            i += 1
            j += 1

        return False


if __name__ == "__main__":
    s = Solution()
    # s1 = "abc"
    # s2 = "lecabee"
    s1 = "abc"
    s2 = "lecaebee"
    result = s.checkInclusion(s1=s1, s2=s2)
    print(result)
