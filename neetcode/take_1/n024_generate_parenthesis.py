from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def recurse(open_count, close_count):
            if open_count == close_count and close_count == n:
                result.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                recurse(open_count=open_count + 1, close_count=close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                recurse(open_count=open_count, close_count=close_count + 1)
                stack.pop()

        recurse(open_count=0, close_count=0)
        return result


if __name__ == "__main__":
    solution = Solution()
    n = 3
    result = solution.generateParenthesis(n=n)
    print(result)
