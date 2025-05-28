#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def winLen(il, ir):
            return ir - il + 1

        res, resLen = [-1, -1], float('inf')

        window = defaultdict(int)
        countT = Counter(t)

        il = 0

        n = len(s)
        
        have = 0
        need = len(countT)

        for ir in range(n):
            c = s[ir]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                checkC = s[il]
                window[checkC] -= 1
                if winLen(il, ir) < resLen:
                    resLen = winLen(il, ir)
                    res = [il, ir]

                if checkC in countT and window[checkC] < countT[checkC]:
                    have -= 1
                il += 1
        
        l, r = res
        return s[l:r+1]
        
# @lc code=end

