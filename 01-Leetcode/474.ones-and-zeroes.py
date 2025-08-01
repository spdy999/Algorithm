#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        lenn = len(strs)
        counter = dict()
        maxx = [0]
        dp = dict()  # (i, cntM, cntN): cnt
        for i, s in enumerate(strs):
            counter[i] = Counter(s)
        # print(counter)

        def dfs(i: int, cntM: int, cntN: int, cnt: int) -> int:
            # print('i:', i, 'cntM:', cntM, 'cntN:',cntN, 'cnt:', cnt)
            if cntM <= m and cntN <= n:
                maxx[0] = max(maxx[0], cnt)
                # print('im 1')
            if (i, cntM, cntN) in dp:
                # print('im 2')
                return dp[(i, cntM, cntN)]
            if cntM > m or cntN > n or i >= lenn:
                # print('im 3')
                return cnt

            dp[(i, cntM, cntN)] = max(dfs(i + 1, cntM + counter[i]['0'],
                                          cntN + counter[i]['1'], cnt + 1), dfs(i + 1, cntM, cntN, cnt))
            # print('dp:', dp)
            return dp[(i, cntM, cntN)]
        dfs(0, 0, 0, 0)

        return maxx[0]


s = Solution()
assert s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4
assert s.findMaxForm(["011", "1", "11", "0", "010", "1", "10", "1", "1", "0", "0", "0", "01111", "011", "11", "00", "11", "10", "1", "0",
                     "0", "0", "0", "101", "001110", "1", "0", "1", "0", "0", "10", "00100", "0", "10", "1", "1", "1", "011", "11", "11", "10"], 44, 39) == 40
# assert s.findMaxForm(["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0", "1", "0", "0110101",
#                      "0", "11", "01", "00", "01111", "0011", "1", "1000", "0", "11101", "1", "0", "10", "0111"], 9, 80) == 40

# @lc code=end
