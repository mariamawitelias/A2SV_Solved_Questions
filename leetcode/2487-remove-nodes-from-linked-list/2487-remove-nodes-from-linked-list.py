# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = None
        curr = head
        while curr:
            while stack and stack.val < curr.val:
                stack = stack.next
            temp = curr.next
            curr.next = stack
            stack = curr
            curr = temp

        prev = None
        while stack:
            temp = stack.next
            stack.next = prev
            prev = stack
            stack = temp
        return prev
