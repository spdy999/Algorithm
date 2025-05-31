#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. find mid node for 2nd linked list
        slow, fast = head, head.next
        while fast and fast.next:  # O(n / 2)
            slow = slow.next
            fast = fast.next.next

        # 2. reverse 2nd linked list
        second = slow.next  # 4 -> 5
        prev = None
        slow.next = None  # 3 -> None
        while second:  # O(n / 2)
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 3. merge 2 linked list
        left = head
        right = prev

        while right:  # O(n / 2)
            tmpL, tmpR = left.next, right.next
            right.next = tmpL
            left.next = right
            left = tmpL
            right = tmpR


# @lc code=end
