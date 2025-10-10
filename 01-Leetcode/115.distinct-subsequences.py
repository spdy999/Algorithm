#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
import sys
sys.setrecursionlimit(100000)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = [0]
        lenS = len(s)
        lenT = len(t)
        cache = dict() # (iS, iT): summ
        # print('s t')
        # print('---')
        def dfs(iS: int, iT: int):
            if iS == lenS or iT == lenT:
                # print('exceed')
                return 0
            # print(iS, iT)
            # print(s[iS], t[iT])
            # print('cache:', cache)
            # print()
            
            if  (iS, iT) in cache:
                # print('cache ', s[iS], iS, t[iT], iT, cache[(iS, iT)])
                # print('found cache: ', cache)
                # print()
                
                return cache[(iS, iT)]

            if iT == lenT - 1 and s[iS] == t[iT]:
                cache[(iS, iT)] = 1
                # print('last reach and cache:', cache)
                summ = 0
                for iS2 in range(iS + 1, lenS): 
                    if (iS2, iT) in cache:
                        continue
                    summ += dfs(iS2, iT)
                cache[(iS, iT)] += summ
                return cache[(iS, iT)]
            if s[iS] == t[iT]:
                # print('found')
                summ = dfs(iS + 1, iT + 1)
                # print('summ dfs:', summ, iS, iT)
                
                for iS2 in range(iS + 1, lenS): 
                    # print('start for1')
                    if (iS2, iT) in cache:
                        continue
                    # if s[iS2] != t[iT] or 
                    #     continue
                    summ += dfs(iS2, iT)
                # print('summ all:', summ)
                cache[(iS, iT)] = summ
                return cache[(iS, iT)]
            else:
                summ = 0
                # print('start for2')
                for iS2 in range(iS + 1, lenS):
                    if (iS2, iT) in cache:
                        continue
                    # if s[iS2] != t[iT] or 
                    #     continue
                    summ += dfs(iS2, iT)

                
                cache[(iS, iT)] = summ
                # print('summ for2: ', summ)
                # print('cache for2:', cache)
                # print('end for2')
                return cache[(iS, iT)]

        for iS in range(lenS):
            if (iS, 0) in cache:
                continue
            # if s[iS] != t[0] or :
            #     continue
            res[0] += dfs(iS, 0)

        # print(cache)
        return res[0]

s = Solution()
assert s.numDistinct(
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == 1

# @lc code=end

