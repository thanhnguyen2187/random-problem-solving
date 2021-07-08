from typing import (
    List,
    Set,
    Dict,
)


class TreeNode:

    def __init__(
        self,
        val: int,
        left=None,
        right=None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def find(
        self,
        val: int,
        trace: Dict[int, int],
    ) -> List[int]:

        path = []

        while True:
            path.append(val)
            if val in trace:
                val = trace[val]
            else:
                break

        return path


    def track(
        self,
        root: TreeNode,
    ) -> dict:
        trace = {}

        stack = [root]
        while len(stack) > 0:
            element = stack.pop()
            if element.left is not None:
                trace[element.left.val] = element.val
                stack.append(element.left)
            if element.right is not None:
                trace[element.right.val] = element.val
                stack.append(element.right)

        return trace


    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode,
    ) -> int:

        trace = self.track(root=root)

        path_p = self.find(trace=trace, val=p.val)
        path_q = self.find(trace=trace, val=q.val)
        path_p.reverse()
        path_q.reverse()
        common_path = [
            value_p
            for value_p, value_q in zip(path_p, path_q)
            if value_p == value_q
        ]

        return TreeNode(common_path[-1])


if __name__ == '__main__':
    solution = Solution()
    print(
        solution.lowestCommonAncestor(
            root=TreeNode(
                val=3,
                left=TreeNode(
                    val=5,
                    left=TreeNode(val=6),
                    right=TreeNode(
                        val=2,
                        left=TreeNode(val=7),
                        right=TreeNode(val=4),
                    )
                ),
                right=TreeNode(
                    val=1,
                    left=TreeNode(val=0),
                    right=TreeNode(val=8),
                ),
            ),
            p=TreeNode(val=5),
            q=TreeNode(val=1),
        )
    )
    print(
        solution.lowestCommonAncestor(
            root=TreeNode(
                val=1,
                left=TreeNode(val=2),
            ),
            p=TreeNode(val=1),
            q=TreeNode(val=2),
        )
    )
