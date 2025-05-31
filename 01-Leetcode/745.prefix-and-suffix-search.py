#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#

# @lc code=start
class WordFilter:
    def __init__(self, words: List[str]):
        self.ps = dict()
        for i, w in enumerate(words):
            for j in range(len(w)):
                pref = w[: j + 1]
                for k in range(len(w)):
                    suff = w[k:]
                    self.ps[pref + "$" + suff] = i

    def f(self, pref: str, suff: str) -> int:
        search = pref + "$" + suff
        if search in self.ps:
            return self.ps[search]
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
# @lc code=end
