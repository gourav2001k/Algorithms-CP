# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next

        prev = None
        cur = head
        while cur != slow:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        cur.next = prev

        out = 0
        while cur:
            out = max(out, cur.val+fast.val)
            cur = cur.next
            fast = fast.next

        return out
