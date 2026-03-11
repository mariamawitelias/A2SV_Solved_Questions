class MyCircularDeque:

    def __init__(self, k: int):
        self.length = k
        self.q = [0] * k
        self.front = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == self.length:
            return False
        
        self.front = (self.front - 1 + self.length) % self.length
        self.q[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.length:
            return False
        
        rear = (self.front + self.size) % self.length
        self.q[rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        
        self.front = (self.front + 1) % self.length
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.q[self.front]

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        rear = (self.front + self.size - 1) % self.length
        return self.q[rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.length