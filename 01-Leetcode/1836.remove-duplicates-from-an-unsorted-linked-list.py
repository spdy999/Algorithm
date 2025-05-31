#
# @lc app=leetcode id=1836 lang=python3
#
# [1836] Remove Duplicates From an Unsorted Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        checkset = set()
        dupset = set()
        pt = head
        prev = head

        # find 2nd -> end duplicate numbers and delete them
        while pt:  # O(n)
            if pt.val in checkset:
                dupset.add(pt.val)
                prev.next = pt.next
                pt = prev.next
                continue
            checkset.add(pt.val)
            prev = pt
            pt = pt.next

        # find each head of each duplicated num
        pt = head
        prev = head
        while pt:  # O(n)
            if pt.val in dupset:
                prev.next = pt.next
                pt = prev.next
                continue
            prev = pt
            pt = pt.next

        # check if head is one of the duplication
        return head.next if head.val in dupset else head


# @lc code=end
