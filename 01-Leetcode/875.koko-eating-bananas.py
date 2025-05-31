#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        maxP = max(piles)
        
        il = 1
        ir = maxP
        minn = ir

        def evalHr(im: int):
            summ = 0
            for p in piles: # O(n)
                summ += int(ceil(p / im))
            return summ

        while il <= ir: # O(log max(piles))
            im = (il + ir) // 2 # k
            eatHr = evalHr(im) # O(n)
            # print('eatHr:', eatHr, 'im:', im, 'minn:', minn)                

            if eatHr <= h:
                minn = min(minn, im)
                ir = im - 1
            else:
                il = im + 1

        return minn

        # bigO = O(n * log max(piles))
        
# @lc code=end

