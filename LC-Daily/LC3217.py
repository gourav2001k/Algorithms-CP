# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        prev, out = None, head
        nums = set(nums)
        while head:
            if head.val in nums:
                if prev:
                    prev.next = head.next
                else:
                    out = head.next
            else:
                prev = head
            head = head.next
        return out
