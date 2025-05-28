#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS right most which is not null?
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
            # print('level:', level)

            for num in level[-1:]: # start from the last
                if num is not None:
                    res.append(num) # Append the right most(the last one which is not None in each level). Then break
                    break

        return res

        # bigO = O(n)
        
# @lc code=end

