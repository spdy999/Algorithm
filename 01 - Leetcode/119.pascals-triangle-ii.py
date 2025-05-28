#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1], [1,1]]
        if rowIndex <= 1:
            return ans[rowIndex]
        rowIndex += 1
        for i in range(2, rowIndex):
            last_row = ans[-1]
            gen_row = [1]
            for j in range(1, i):
                gen_row.append(last_row[j-1] + last_row[j])
                continue
            gen_row.append(1)
            ans.append(gen_row)
        
        return ans[-1]
        
# @lc code=end

