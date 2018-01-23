


class Queue:
    def __init__(self, max_size):
        self.queue = [None] * max_size

        self.capacity = max_size

        self.size = 0

        self.head = -1
        self.tail = 0

    def enqueue(self, x):
        if self.is_full():
            return
        self.size += 1
        self.head = (self.head + 1) % self.capacity
        self.queue[self.head] = x

    def dequeue(self):
        if self.is_empty():
            return
        self.size -= 1
        element = self.queue[self.tail]
        self.tail = (self.tail + 1) % self.capacity
        return element

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity


class Stack:
    def __init__(self, max_size):
        self.queue1 = Queue(max_size)
        self.queue2 = Queue(max_size)
        self.capacity = max_size

    def insert(self, x):
        if self.is_full():
            return

        self.queue2.enqueue(x)
        while not self.queue1.is_empty():
            self.queue2.enqueue(self.queue1.dequeue())

        self.queue2, self.queue1 = self.queue1, self.queue2

    def pop(self):
        if self.is_empty():
            return
        return self.queue1.dequeue()

    def is_full(self):
        return self.queue1.size + self.queue2.size == self.capacity

    def is_empty(self):
        return self.queue1.size + self.queue2.size == 0


class Stack2:
    def __init__(self, max_size):
        self.queue = Queue(max_size)
        self.capacity = max_size

    def insert(self, x):
        if self.is_full():
            return
        self.queue.enqueue(x)
        for _ in range(self.queue.size - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self):
        if self.is_empty():
            return
        return self.queue.dequeue()

    def is_full(self):
        return self.queue.size == self.capacity

    def is_empty(self):
        return self.queue.size == 0


if __name__ == '__main__':
    test_stack = []
    stack = Stack(1000)
    stack2 = Stack2(1000)

    import random
    for _ in range(1000):
        rd_int = random.randint(0, 1000)
        test_stack.append(rd_int)
        stack.insert(rd_int)
        stack2.insert(rd_int)
        if random.random() < 0.3:
            a = stack.pop()
            b = test_stack.pop()
            c = stack2.pop()
            print a
            assert a == b == c