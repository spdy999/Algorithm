```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        last_house = n - 1
        # mem = {}

        if n <= 3:
            return max(nums)
        
        def rec(i: int, summ: int, is_first_house_robbed: bool, check: List[int]) -> int:
            # if i in mem:
            #     return summ + mem[i]
            if i == last_house - 1 and is_first_house_robbed:
                return summ + nums[i]            
            if i == last_house and is_first_house_robbed:
                return summ
            if i == last_house and not is_first_house_robbed:
                return summ + nums[i]
            if i > last_house:
                return summ
            check.append(nums[i])
            maxi = max(rec(i+2, summ + nums[i], is_first_house_robbed, check), rec(i+3, summ + nums[i], is_first_house_robbed, check))
            # mem[i] = maxi - summ
            return maxi
            
        return max(rec(0, 0, True, list()), rec(1, 0, False, list()))
```