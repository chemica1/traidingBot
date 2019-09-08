class CircularQueue():

    def __int__(self, max=1000):
        self.max = max
        self.queue = [None] * self.max
        self.size = self.front = 0
        self.rear = None

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        if self.is_full():
            raise Exception("Queue is Full")

        if self.rear == None:
            self.rear = 0
        else:
            self.rear = self.next_index(self.rear)

        self.queue[self.rear] = data
        self.size += 1
        return self.queue[self.rear]

    def deque(self):
        if self.is_empty():
            raise
            Exception('Queue is empty')
            self.queue[self.front] = None
            self.front = self.next_index(self.front)
            return self.queue[self.front]

    def display(self):
        print(self.queue)

if __name__ == '__main__':
    cq = CircularQueue()
    cq.display()
    print(cq.enqueu())
    print(cq.enqueu())
    print(cq.enqueu())
    print(cq.enqueu())
    cq.display()
    print(cq.deque())
    print(cq.deque())
    cq.display()
    print(cq.enqueue())
    print(cq.enqueue())
    cq.display()