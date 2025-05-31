#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket-sort => TC: O(n) ???

        n = len(nums)
        count_num = Counter(nums) # O(n)
        freq = [[] for _ in range(n + 1)]
        ans = []

        for num, count in count_num.items(): # O(n)
            freq[count].append(num)

        for i in range(n, 0, -1): # O(n)
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        
# @lc code=end

