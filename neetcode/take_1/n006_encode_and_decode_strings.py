from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        prefix = str(len(strs))
        result = [prefix]
        result.extend(strs)
        return "\0".join(result)

    def decode(self, s: str) -> List[str]:
        parts = s.split("\0")
        length = int(parts[0])

        if length == 0:
            return []

        return parts[1:]


if __name__ == "__main__":
    print("abc".rjust(6))
    # s = Solution()
    # nums = []
    # result = s.solution(nums=nums)
    # print(result)
