#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = head
        cur = head.next

        while cur:
            # if sorted
            if prev.val <= cur.val:
                prev = cur
                cur = cur.next
                continue

            tmp = dummy
            while tmp.next.val < cur.val:
                tmp = tmp.next
            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next

        return dummy.next

# @lc code=end

