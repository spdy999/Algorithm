#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, subNode) -> bool:
            if node is None and subNode is None:
                return True

            if node and subNode:
                if node.val != subNode.val:
                    return False
            if node and subNode is None:
                return False
            if node is None and subNode:
                return False

            if dfs(node.left, subNode.left) and dfs(node.right, subNode.right):
                return True

        q = deque()
        q.append(root)
        
        while q:
            lenQ = len(q)
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    if node.val == subRoot.val:
                        if dfs(node, subRoot):
                            return True

        return False

        
# @lc code=end

