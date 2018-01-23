# 基于链表和堆的组合结构实现能够维护最大值的队列

class QueueNode:
    def __init__(self):
        self.val = None
        self.previous = None
        self.heap_idx = None
        self.next = None

class MaxHeap:
    def __init__(self):
        self._arr = []

    def insert(self, queue_node):
        self._arr.append(queue_node)
        queue_node.heap_idx = len(self._arr) - 1
        self._shift_up(len(self._arr) - 1)

    def extract(self, idx):
        # print("remove idx ", idx)
        # print("self.arr", self._arr)
        # print("arr (idx, val) in object", map(lambda x: (x.heap_idx, x.val), self._arr))
        self.swap(idx, len(self._arr) - 1)

        poped_ele = self._arr.pop()
        self._shift_down(idx)
        return poped_ele

    def get_max(self):
        return self._arr[0].val

    def _shift_up(self, i):
        if i <= 0:
            return
        parent_idx = self.parent(i)
        parent_node = self._arr[parent_idx]
        if parent_node.val < self._arr[i].val:
            self.swap(parent_idx, i)
            self._shift_up(parent_idx)

    def _shift_down(self, i):
        max_idx = i
        left_child_idx = self.left_child(i)
        right_child_idx = self.right_child(i)
        # print("left {}, right {}, length of arr {}".format(left_child_idx, right_child_idx, len(self._arr)))
        if left_child_idx < len(self._arr) and self._arr[left_child_idx].val > self._arr[max_idx].val:
            max_idx = left_child_idx
        if right_child_idx < len(self._arr) and self._arr[right_child_idx].val > self._arr[max_idx].val:
            max_idx = right_child_idx

        if max_idx != i:
            self.swap(i, max_idx)
            self._shift_down(max_idx)

    def parent(self, i):
        return ((i + 1) // 2) - 1

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        node_i = self._arr[i]
        node_j = self._arr[j]
        node_i.heap_idx = j
        node_j.heap_idx = i
        self._arr[j], self._arr[i] = node_i, node_j


class ChainQueue:
    def __init__(self, max_size):
        # self._queue = []
        self.capacity = max_size
        self.size = 0
        self.head_pointer = QueueNode()
        self.tail_pointer = QueueNode()
        self.heap = MaxHeap()

        self.head_pointer.next = self.tail_pointer
        self.tail_pointer.previous = self.head_pointer

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, x):
        if self.is_full():
            print "the queue is full"
            return
        print("enqueue ele {} into queue".format(x))
        node = QueueNode()
        node.val = x

        last_queue_ele = self.tail_pointer.previous
        last_queue_ele.next = node

        node.next = self.tail_pointer
        node.previous = last_queue_ele

        self.tail_pointer.previous = node

        self.heap.insert(node)

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print "the queue is empty"
            return

        first_ele = self.head_pointer.next
        second_ele = first_ele.next

        self.head_pointer.next = second_ele
        second_ele.previous = self.head_pointer

        # print("the first_ele ele val {} has idx {} in heap".format(first_ele.val, first_ele.heap_idx))
        dequeued_ele = self.heap.extract(first_ele.heap_idx)
        # print ("dequeued ele val is {} but target ele val is {}".format(dequeued_ele.val, first_ele.val))
        assert dequeued_ele.val == first_ele.val

        self.size -= 1

        return first_ele.val

    def max_val(self):
        if self.is_empty():
            print "the queue is empty"
            return
        return self.heap.get_max()


def test_chain_queue():
    mq = ChainQueue(5)

    mq.enqueue(5)
    print "max v", mq.max_val()


    mq.enqueue(2)
    print "max v", mq.max_val()
    print mq.max_val()

    mq.enqueue(1)
    print "max v", mq.max_val()

    mq.enqueue(3)
    print "max v", mq.max_val()
    print mq.max_val()
    mq.enqueue(4)
    print "max v", mq.max_val()
    print mq.max_val()

    print(mq.dequeue())
    print "max v", mq.max_val()
    print(mq.dequeue())
    print "max v", mq.max_val()
    print(mq.dequeue())
    print "max v", mq.max_val()

    print(mq.dequeue())
    print "max v", mq.max_val()

    print(mq.dequeue())
    print "max v", mq.max_val()


if __name__ == '__main__':
    test_chain_queue()
