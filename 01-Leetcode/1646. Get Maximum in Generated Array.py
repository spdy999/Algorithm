#
# @lc app=leetcode id=1646 lang=python3
#
# [1646] Get Maximum in Generated Array
#

# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        nums = [0] * (n+1)
        nums[0] = 0
        nums[1] = 1
        maxi = 1
        last_ind = ceil(n/2) + 1 if n % 2 == 0 else ceil(n/2)
        for i in range(1, last_ind):
            even = 2*i
            odd = 2*i + 1
            # print('i:', i, 'even:', even, 'odd:', odd)
            nums[even] = nums[i]
            maxi = max(maxi, nums[even])
            if odd < n + 1:
                nums[odd] = nums[i] + nums[i + 1]
                maxi = max(maxi, nums[odd])
            # print(nums)


        return maxi
        
# @lc code=end

