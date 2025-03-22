from typing import List


def match_opening(char: str):
    match char:
        case ")":
            return "("
        case "}":
            return "{"
        case "]":
            return "["
        case _:
            raise ValueError("invalid char: " + char)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            match char:
                case "(" | "{" | "[":
                    stack.append(char)
                case ")" | "}" | "]":
                    if len(stack) > 0 and stack[-1] == match_opening(char=char):
                        stack.pop()
                    else:
                        return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    s = "()(){}({})("
    result = solution.isValid(s=s)
    print(result)
