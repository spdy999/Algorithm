#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = dummy.next
        nxt = dummy.next
        while nxt:
            # 1. move 
            for i in range(k):
                nxt = nxt.next
                if nxt is None:
                    if i < k - 1:
                        return dummy.next # last set no need to be reversed
                    else:
                        break # last list need to be reverse due to len == k
                
            conj = self.reverse(cur, nxt)
            prev.next = conj

            for i in range(k):
                prev = prev.next
            prev.next = nxt
            cur = prev.next

        return dummy.next

    def reverse(self, cur, nxt):
        prev = None
        while cur != nxt:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
        
# @lc code=end

