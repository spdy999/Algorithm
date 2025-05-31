#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        # bigO = O(n)
        if root is None:
            return 0

        q = deque()
        q.append(root)
        depth = 0
        while q:
            lenQ = len(q)
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)

            depth += 1
        return depth - 1


        
# @lc code=end

