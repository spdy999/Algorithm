Project:: Leetcode
Progress:: Completed?? Try neet code it's easier and faster
Date:: 2024-06-21
Difficulty:: #Medium 
Time:: `O(2^n)`
Space:: `O(n)`
Tags:: 
Topic:: [[DP]]
Techniques:: [[DP#Bottom-Up]]
Sites:: [Leetcode](https://leetcode.com/problems/house-robber-ii/description/)
Walkthrough:: [House Robber II - Dynamic Programming - Leetcode 213 - YouTube](https://www.youtube.com/watch?v=rWAJCfYYOvM)
Related problems:: [[198. House Robber]]
Companies:: #Company/Google
Code:: 
Note:: DP from neet is easy to read and memorize but a bit confused to understand the concept (why it looks like Greedy?)

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