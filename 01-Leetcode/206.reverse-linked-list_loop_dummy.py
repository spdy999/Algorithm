#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        prev = head
        cur = head.next

        while cur:
            prev.next = cur.next
            cur.next = dummy.next
            dummy.next = cur

            cur = prev.next

        return dummy.next

# @lc code=end
