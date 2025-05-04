

class Solution:
    def climbStairs(self, n: int) -> int:
        ns = [0, 1]

        if n < 2:
            return ns[n]

        for _ in range(n):
            ns.append(ns[-1] + ns[-2])

        return ns[-1]


if __name__ == "__main__":
    solution = Solution()
    nums = []
    result = solution.solution(nums=nums)
    print(result)
