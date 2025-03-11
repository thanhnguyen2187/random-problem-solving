from typing import List
from itertools import groupby
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_dict = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            grouped_dict[key].append(str)

        return [value for value in grouped_dict.values()]


if __name__ == "__main__":
    s = Solution()
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    result = s.groupAnagrams(strs=strs)
    print(result)
