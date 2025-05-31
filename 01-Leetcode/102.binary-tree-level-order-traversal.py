#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return root

        q = deque()
        q.append(root)
        res = []
         
        while q:
            lenQ = len(q)
            level = []
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if len(level) is not 0:
                res.append(level)
                
        return res
        # bigO = O(n)

# @lc code=end

