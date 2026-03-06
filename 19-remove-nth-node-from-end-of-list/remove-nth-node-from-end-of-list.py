class Solution:    
    def removeNthFromEnd(self, head, n):
        l, r = head, head
        for _ in range(n):
            r = r.next
        if r is None:
            return head.next
        while r.next:
            r = r.next
            l = l.next
        l.next = l.next.next
        return head