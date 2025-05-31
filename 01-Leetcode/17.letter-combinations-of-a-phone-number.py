#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        if n == 0:
            return res

        digitToStrs = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9': 'wxyz'
        }
        
        def dfs(level: int, comb: str): # Adapt from 559. Maximum Depth of N-ary Tree
            if level >= n:
                res.append(comb)
                return

            digit = digits[level]
            letters = digitToStrs[digit]
            for c in letters: # abc 
                dfs(level + 1, comb + c) # traverse through node children, backtracking 

        dfs(0, "")
        return res
        
        # bigO = O(3^n)
        
# @lc code=end

