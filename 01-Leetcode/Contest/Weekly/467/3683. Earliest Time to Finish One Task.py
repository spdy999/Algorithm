class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        minn = float('inf')
        for s, t in tasks:
            minn = min(minn, s + t)
        return minn