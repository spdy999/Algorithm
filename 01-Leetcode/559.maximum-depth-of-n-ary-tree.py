#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
            
        def dfs(r: 'Node', level: int) -> int:
            if len(r.children) == 0:
                return level + 1

            children = r.children
            return max([dfs(c, level + 1) for c in children])
        
        return dfs(root, 0)
        
        
# @lc code=end

