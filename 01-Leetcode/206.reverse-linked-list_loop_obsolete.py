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
        prev = None
        cur = head # 0
        while cur:
            nxt = cur.next # 1
            cur.next = prev # None 
            prev = cur     # 0
            cur = nxt      # 1  
        return prev
        
# @lc code=end

