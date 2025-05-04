from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)
        for char in ransomNote:
            counter[char] -= 1
        return all(char_count >= 0 for char_count in counter.values())


if __name__ == "__main__":
    solution = Solution()
    nums = []
    result = solution.solution(nums=nums)
    print(result)
