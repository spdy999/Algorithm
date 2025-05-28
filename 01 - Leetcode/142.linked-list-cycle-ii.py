#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        check = set()

        while cur:  # O(n)
            if cur in check:
                return cur
            check.add(cur)
            cur = cur.next
        return None
        
# @lc code=end

