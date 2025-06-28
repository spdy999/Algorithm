#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # - reverse left half linklist and find the head of the right half linklist -> O(n)
        # - cycle through those 2 list and summ and find maxx -> O(n)
        # - return maxx

        # Floyd's tortoise and hare
        f, sr = head, head

        # reverse linkedlist's left half
        sl = None  # prev
        cur = head

        # Floyd's tortoise and hare
        while f and f.next:
            sr = sr.next
            f = f.next.next

            # reverse linkedlist's left half
            tmp_nxt = cur.next
            cur.next = sl
            sl = cur
            cur = tmp_nxt

        maxx = 0
        while sl and sr:
            summ = sl.val + sr.val
            maxx = max(summ, maxx)

            sl = sl.next
            sr = sr.next

        return maxx

# @lc code=end

