#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 2sum + prefix sum

        cnt = 0
        dictInd = defaultdict(int)  # { prefixR: cnt }
        dictInd[0] = 1

        prefixR = 0
        for num in nums:
            prefixR += num
            prefixL = prefixR - k  # k = prefixR - prefixL = subarraySum

            cnt += dictInd[prefixL]
            dictInd[prefixR] += 1

        return cnt
        
        
# @lc code=end

