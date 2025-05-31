#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            anagrams["".join(sorted(s))].append(s)

        return list(anagrams.values())


assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
    ["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
assert Solution().groupAnagrams([""]) == [[""]]
assert Solution().groupAnagrams(["a"]) == [["a"]]

# @lc code=end
