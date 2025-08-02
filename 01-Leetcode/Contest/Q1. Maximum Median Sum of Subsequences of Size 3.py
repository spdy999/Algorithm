from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
    
        # Step 2: Calculate the sum of medians
        n = len(nums)
        median_sum = 0
        # print(nums)
        
        # We take the medians from the last third of the sorted array
        for i in range(n // 3, n, 2):
            # print('i:', i, 'nums:',nums[i])
            median_sum += nums[i]
        
        return median_sum

s = Solution()
assert s.maximumMedianSum([1,2,3,4,5,6,7,8,9]) == 18
assert s.maximumMedianSum([1,1,10,10,10,10]) == 20
assert s.maximumMedianSum([2,1,3,2,1,3]) == 5