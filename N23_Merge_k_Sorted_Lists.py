# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

### Solution 1: Heap
class Heap:
    def __init__(self):
         self._arr = []
    def insert(self, x):
        # print("insert node with x {}".format(x.val))
        self._arr.append(x)
        self.shift_up(len(self._arr)-1)
        # print("current array is {}".format(map(lambda a: a.val, self._arr)))
    def extract_min(self):
        min_node = self._arr[0]
        if min_node.next:
            self._arr[0] = min_node.next
        else:
            self.swap(0, len(self._arr)-1)
            self._arr.pop()
        # print("current array is {}".format(map(lambda a: a.val, self._arr)))
        self.shift_down(0)
        # print("after shift down current array is {}".format(map(lambda a: a.val, self._arr)))
        min_node.next = None
        return min_node
    def get_size(self):
        return len(self._arr)
    def shift_up(self, i):
        if i == 0:
            return
        # print("compare i {} val {} with parent_i {}, val {}".format(i-1, self._arr[i-1].val, self.parent(i)-1, self._arr[self.parent(i)-1].val))
        if self._arr[i].val < self._arr[self.parent(i)].val:
            self.swap(i, self.parent(i))
            self.shift_up(self.parent(i))
    def shift_down(self, i):
        # i is 0 based idx
        max_idx = i
        left_child = self.left_child(i)
        right_child = self.right_child(i)
        # print("i {}, left {}, right {}".format(max_idx, left_child, right_child))

        if left_child < self.get_size() and self._arr[left_child].val < self._arr[max_idx].val:
            max_idx = left_child

        if right_child < self.get_size() and self._arr[right_child].val < self._arr[max_idx].val:
            max_idx = right_child

        if i != max_idx:
            self.swap(i, max_idx)
            self.shift_down(max_idx)

    def parent(self, i):
        a = i + 1
        return (a // 2) - 1
    def left_child(self, i):
        a = i + 1
        return 2*a - 1
    def right_child(self, i):
        a = i + 1
        return 2*a
    def swap(self, i, j):
        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]

class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = Heap()
        for _list in lists:
            if not _list:
                continue
            heap.insert(_list)
        head_node = point = ListNode(0)
        while heap.get_size()>0:

            point.next = heap.extract_min()
            # print("extract {}".format(current_node.next.val))
            point = point.next

        return head_node.next


### Solution 2: divide and conquer
def merge2list(ls1, ls2):
    head = point = ListNode(0)
    while ls1 and ls2:
        val_ls1 = ls1.val
        val_ls2 = ls2.val
        if val_ls1 < val_ls2:
            point.next = ListNode(val_ls1)
            ls1 = ls1.next
        else:
            point.next = ListNode(val_ls2)
            ls2 = ls2.next
        point = point.next
    if ls1:
        point.next = ls1
    else:
        point.next = ls2
    return head.next

class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return lists
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return merge2list(lists[0], lists[1])
        m = len(lists) // 2
        return merge2list(self.mergeKLists(lists[:m]), self.mergeKLists(lists[m:]))


def convert_list_to_singly_liked_list(_l):
    current_node = ListNode(_l.pop())
    while _l:
        _temp_node = ListNode(_l.pop())
        _temp_node.next = current_node
        current_node = _temp_node
    return current_node


if __name__ == '__main__':
    # t1 = convert_list_to_singly_liked_list([1, 3, 5, 10, 18])
    # t2 = convert_list_to_singly_liked_list([2, 4, 6, 13, 44])
    # t3 = convert_list_to_singly_liked_list([2, 3, 9, 11, 15])
    t1 = convert_list_to_singly_liked_list([1, 2, 2])
    t2 = convert_list_to_singly_liked_list([1, 1, 2])
    cls = Solution1()
    cur_node =  cls.mergeKLists([t1, t2])
    while cur_node.next is not None:
        print cur_node.val,
        cur_node = cur_node.next
    print("finish")


