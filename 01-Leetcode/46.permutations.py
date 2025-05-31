#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack_dfs(head, tail):
            if len(tail) == n:
                res.append(tail)
                return

            for i in range(len(head)):
                new_head = head[:i] + head[i + 1:]
                new_tail = tail + [head[i]]
                backtrack_dfs(new_head, new_tail)

        backtrack_dfs(nums, [])
        return res


assert Solution().permute([1, 2, 3]) == [[1, 2, 3], [1, 3, 2],
                                         [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# @lc code=end
