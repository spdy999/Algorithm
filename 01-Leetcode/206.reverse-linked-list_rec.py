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
        # bigO = O(n)
        
        def rec(prev, cur):
            if cur is None:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return rec(prev, cur)
        return rec(None, head)
        
# @lc code=end

