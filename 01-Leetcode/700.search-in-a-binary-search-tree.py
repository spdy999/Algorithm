#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return None
            if val == node.val:
                return node
            elif val >= node.val:
                return dfs(node.right)
            elif val <= node.val:
                return dfs(node.left)
            return None
        return dfs(root)
        
# @lc code=end

