#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1Count = dict()
        s2Count = dict()
        

        for lt in string.ascii_lowercase:
            s1Count[lt] = 0
            s2Count[lt] = 0

        for i in range(len_s1):
            s1Count[s1[i]] += 1
            s2Count[s2[i]] += 1
        
        def intersection():
            return len(s1Count.items() & s2Count.items()) # O(26)

        matches = intersection()  # intersection
        for i in range(len_s1, len_s2): # O(len_s2 - len_s1)
            if matches == 26: return True

            s2Count[s2[i]] += 1
            s2Count[s2[i - len_s1]] -=1
            matches = intersection() # O(26)
            
        return matches == 26

        # bigO = O(26n)

        
# @lc code=end

