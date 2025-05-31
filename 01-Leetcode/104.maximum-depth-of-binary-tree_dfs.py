#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(r: TreeNode, level: int):
            if r is None:
                return level

            return max(dfs(r.left, level + 1), dfs(r.right, level + 1))

        return dfs(root, 0)


# @lc code=end
