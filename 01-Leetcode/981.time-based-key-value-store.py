#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value)) # Sorted

    def get(self, key: str, timestamp: int) -> str:
        vals = self.data[key]
        l = 0
        r = len(vals) - 1
        ans = ""

        while l <= r: # O(log n)
            m = (l + r) // 2
            tm, vm = vals[m]
            if tm <= timestamp:
                ans = vm
                l = m + 1
            else:
                r = m - 1
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

