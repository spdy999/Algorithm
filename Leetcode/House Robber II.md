Project:: Leetcode
Progress:: Completed
Date:: 2024-06-21
Difficulty:: #Medium 
Time:: `O(2^n)`
Space:: `O(n)`
Tags:: 
Topic:: [[DP]]
Techniques:: [[DP]]
Sites:: [Leetcode](https://leetcode.com/problems/house-robber-ii/description/)
Walkthrough:: 
Related problems:: 
Companies:: #Company/Google
Code:: 
Note:: I think I wrote it by myself but should read from Neet for a better way

---

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        last_ind = n - 2

        if n <= 2:
            return max(nums)
        
        def rec(i: int, summ: int, nums, mem) -> int:
            if i in mem:
                return summ + mem[i]
            if i > last_ind:
                return summ
            if i == last_ind or i == last_ind - 1:
                return summ + nums[i]
            else:
                maxi = max(rec(i+2, summ + nums[i], nums, mem), rec(i+3, summ + nums[i], nums, mem))
                mem[i] = maxi - summ
                return maxi

        nums1 = nums[:-1]
        nums2 = nums[1:] 
        return max(max(rec(0, 0, nums1, dict()), rec(1, 0, nums1, dict())),
        max(rec(0, 0, nums2, dict()), rec(1, 0, nums2, dict())))
```