# 基于两个栈组合的方式实现队列
# 该队列可以维护最大值

class MaxStack:
    def __init__(self):
        self.nums = []
        self.max_arr = []

    def insert(self, x):
        if len(self.nums) == 0:
            self.nums.append(x)
            self.max_arr.append(x)
        else:
            self.nums.append(x)
            self.max_arr.append(max(x, self.max_arr[-1]))

    def is_empty(self):
        return len(self.nums) == 0

    def pop(self):
        if self.is_empty():
            raise Exception, "the stack is empty"
        self.max_arr.pop()
        return self.nums.pop()

    def get_max(self):
        if self.is_empty():
            raise Exception, "the stack is empty"
        return self.max_arr[-1]


class MaxQueue:
    def __init__(self):
        self.stackA = MaxStack()
        self.stackB = MaxStack()

    def enqueue(self, x):
        self.stackA.insert(x)

    def dequeue(self):
        if self.is_empty():
            raise Exception, "the queue is empty"
        if self.stackB.is_empty():
            while not self.stackA.is_empty():
                self.stackB.insert(self.stackA.pop())
        return self.stackB.pop()

    def is_empty(self):
        return self.stackA.is_empty() and self.stackB.is_empty()

    def get_max(self):
        if self.is_empty():
            raise Exception, "the queue is empty"

        max_b = -float('inf')
        if not self.stackB.is_empty():
            max_b = self.stackB.get_max()

        max_a = -float('inf')
        if not self.stackA.is_empty():
            max_a = self.stackA.get_max()

        return max(max_a, max_b)

if __name__ == '__main__':
    import random

    test_q = MaxQueue()
    base_q = []

    for _ in range(1000):
        random_ele = random.randint(0, 10000)
        test_q.enqueue(random_ele)
        base_q.append(random_ele)
        max_a = test_q.get_max()
        max_b = max(base_q)
        assert max_a == max_b, "max_a {}, max_b {}, stack_a max {}, stack b max {}".format(max_a, max_b, test_q.stackA.get_max(), test_q.stackB.get_max())
        if random.random() < 0.1 and len(base_q) > 0:
            # print(test_q.stackA.nums)
            # print(test_q.stackB.nums)
            # print(test_q.stackA.get_max(), test_q.stackB.get_max())
            a = test_q.dequeue()
            b = base_q.pop(0)
            assert a == b

    for _ in range(100):
        a = test_q.dequeue()
        b = base_q.pop(0)
        assert a == b, "a is {}, b is {}".format(a, b)
        assert test_q.get_max() == max(base_q)