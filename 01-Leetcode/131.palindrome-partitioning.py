#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        part = []

        def isPalin(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i: int):
            if i >= n:
                res.append(part.copy())
                return

            for j in range(i, n):  # Horizontal
                if isPalin(i, j):
                    part.append(s[i: j + 1])
                    backtrack(j + 1)  # Vertical
                    part.pop()  # Backtrack
        backtrack(0)
        return res


s = Solution()
assert s.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
assert s.partition("a") == [["a"]]
assert s.partition("abcd") == [["a", "b", "c", "d"]]


# @lc code=end
