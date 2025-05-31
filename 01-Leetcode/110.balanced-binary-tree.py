#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    isBalance = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # DFS
        def dfs(node):
            if self.isBalance == False:
                return 0 # This number is bullshit. I return it for not breaking the code. it might be calculated wrong somewhere but that result will not effect shit in this code
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                self.isBalance = False

            return 1 + max(left, right)
        
# @lc code=end

