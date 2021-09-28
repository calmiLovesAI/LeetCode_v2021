# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 解法一：DFS，时间复杂度：O(N^2)
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root is None:
            return 0

        ret = self._rootSum(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret

    def _rootSum(self, root: TreeNode, targetSum: int) -> int:
        if root is None:
            return 0
        ret = 0
        if root.val == targetSum:
            ret += 1
        ret += self._rootSum(root.left, targetSum - root.val)
        ret += self._rootSum(root.right, targetSum - root.val)
        return ret


# 解法二：前缀和，时间复杂度：O(N)
class Solution2:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)
