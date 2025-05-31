#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect = defaultdict(list)

        # O(n * klogk)
        for i,s in enumerate(strs): # O(n)
            collect[''.join(sorted(s))].append(strs[i]) # sorted() => O(klogk)
            
        return collect.values()
        
# @lc code=end

