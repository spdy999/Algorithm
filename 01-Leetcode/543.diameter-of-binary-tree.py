#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return -1
            
            l = dfs(node.left)
            r = dfs(node.right)
            
            self.maxi = max(self.maxi, 2 + l + r)

            return 1 + max(l, r)
        
        dfs(root)
        return self.maxi
        
# @lc code=end

