#
# @lc app=leetcode id=1343 lang=python3
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        summ = sum(arr[:k])
        avg = summ / k
        cnt = 1 if avg >= threshold else 0
        il = 0

        for ir in range(k, n):
            summ = summ - arr[il] + arr[ir]
            avg = summ / k
            if avg >= threshold:
                cnt += 1
            il += 1
        return cnt


s = Solution()
assert s.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3
assert s.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5) == 6

# @lc code=end
