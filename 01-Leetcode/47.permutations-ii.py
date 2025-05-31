#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        def backtrack_dfs(head, tail):
            if len(tail) == n:
                res.add(tuple(tail))
                return

            for i in range(len(head)):
                new_head = head[:i] + head[i + 1:]
                new_tail = tail + [head[i]]
                backtrack_dfs(new_head, new_tail)

        backtrack_dfs(nums, [])
        return list(res)


# @lc code=end
