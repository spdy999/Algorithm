# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)
        if n <= 1:
            return pairs
        
        m = n // 2
        l = self.mergeSort(pairs[:m])
        r = self.mergeSort(pairs[m:])
        return self.merge(l, r)
    
    def merge(self, l: List[Pair], r: List[Pair]) -> List[Pair]:
        ans = []
        while l and r:
            if l[0].key <= r[0].key:
                ans.append(l.pop(0))
            else:
                ans.append(r.pop(0))
        ans = ans + l + r
        return ans
