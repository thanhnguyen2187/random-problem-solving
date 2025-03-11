from typing import List
from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = defaultdict(list)

        max_ = 1
        for key, value in counter.items():
            buckets[value].append(key)
            max_ = max(max_, value)

        result = []
        i = max_
        while len(result) < k and i > 0:
            if i in buckets:
                result.extend(buckets[i])
            i -= 1

        return result


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3, 4, 4, 4]
    k = 3
    result = s.topKFrequent(nums=nums, k=k)
    print(result)
