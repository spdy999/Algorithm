#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#


# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(len(nums1)):
                nums1[i:] = nums2[i:]
            return

        start = 0
        while len(nums2) != 0 and start < m + n:
            # print(start, nums1, nums2)
            for i in range(start, len(nums1) - 1):
                if len(nums2) == 0:
                    break
                if nums2[0] <= nums1[i]:
                    nums1.insert(i, nums2.pop(0))
                    nums1.pop()
                    break
                elif nums1[i] < nums2[0] < nums1[i + 1]:
                    nums1.insert(i + 1, nums2.pop(0))
                    nums1.pop()
                    break
            start += 1
        if len(nums2) != 0:
            nums1[-len(nums2) :] = nums2[0:]


# @lc code=end
