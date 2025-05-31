#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 1
        
        maxCnt = 2 if arr[0] != arr[1] else 1
        il = 0
        lessThan = arr[0] < arr[1]

        for ir,num in enumerate(arr[:-1], start=1):
            less = True if arr[ir - 1] < arr[ir] else False
            more = True if arr[ir - 1] > arr[ir] else False
            # <, <                                       # >, >
            if (less and lessThan) or (more and not lessThan):
                il = ir - 1
                maxCnt = max(2, maxCnt)
            # <, >                                       # >, <
            elif (less and not lessThan) or (more and lessThan):
                maxCnt = max(ir - il + 1, maxCnt)
            else:
                il = ir
                maxCnt = max(1, maxCnt)


            lessThan = less


        return maxCnt

        
# @lc code=end

