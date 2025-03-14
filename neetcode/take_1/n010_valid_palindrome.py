from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alphanum = "".join(char.lower() for char in s if char.isalnum())
        n = len(s_alphanum)
        for i in range(n // 2):
            char_left = s_alphanum[i]
            char_right = s_alphanum[n - i - 1]
            if char_left != char_right:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    s_ = "Was it a car or a cat I saw?"
    result = s.isPalindrome(s=s_)
    print(result)
