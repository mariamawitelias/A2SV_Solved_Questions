
class ListNode: 
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next
class MyLinkedList(object):
    def __init__(self):
        self.head = ListNode(-1)
        self.size = 0
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1 
        curr = self.head.next
        for _ in range(index):
            curr = curr.next 
        return curr.val
    def addAtHead(self, val):
        self.addAtIndex(0, val)
    def addAtTail(self, val):
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index, val):
        if index > self.size:
            return 
        dummy = self.head
        prev, curr = dummy, self.head.next
        for _ in range(index):
            prev = curr
            curr = curr.next
        mew = ListNode(val)
        prev.next = mew
        mew.next = curr
        self.size += 1
    def deleteAtHead(self):
        self.deleteAtIndex(0)
    def deleteAtTail(self):
        self.deleteAtIndex(self.size - 1)
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return 
        dummy = self.head
        prev, curr = dummy, self.head.next
        for _ in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        self.size -= 1










# def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self def self self 







