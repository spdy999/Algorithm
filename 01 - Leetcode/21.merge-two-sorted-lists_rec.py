#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val <= list2.val:
            merged = self.mergeTwoLists(list1.next, list2)
            list1.next = merged
            return list1
        else:
            merged = self.mergeTwoLists(list1, list2.next)
            list2.next = merged
            return list2
        
# @lc code=end

