import copy
import random
import heapq
import time
import numpy as np

def swap(arr, i, j):
    # print("swap {} idx {} and {}".format(arr, i, j))
    arr[i], arr[j] = arr[j], arr[i]
    # print("after swap", arr)


def min_idx(_arr):
    min_val = float('inf')
    idx = len(_arr)
    for i, v in enumerate(_arr):
        if v < min_val:
            min_val = v
            idx = i
    return idx


def select_sort(target_array):
    for i in range(len(target_array)-1):
        _min = min_idx(target_array[i:])
        swap(target_array, i, _min+i)
    return target_array


def quick_sort(target_array):
    if len(target_array) <= 1:
        return target_array

    idx = random.randint(0, len(target_array)-1)

    base_val = target_array[idx]

    larger = []
    smaller = []
    equals = []
    for ele in target_array:
        if ele > base_val:
            larger.append(ele)
        elif ele < base_val:
            smaller.append(ele)
        else:
            equals.append(ele)

    return quick_sort(smaller) + equals + quick_sort(larger)


def quick_sort2(nums):
    quick_sort_util(nums, 0, len(nums)-1)
    return nums


def quick_sort_util(nums, start, end):
    if end - start <= 0:
        return
    idx = random.randint(start, end)
    pivot = nums[idx]
    swap(nums, start, idx)

    i = start
    j = end
    while j > i:
        while nums[j] > pivot and j > i:
            j -= 1
        swap(nums, i, j)
        while nums[i] <= pivot and j > i:
            i += 1
        swap(nums, i, j)
    quick_sort_util(nums, start, i-1)
    quick_sort_util(nums, i+1, end)



def bubble_sort(target_array):

    for last in range(len(target_array), 0, -1):
        for i in range(1, last):
            if target_array[i] < target_array[i-1]:
                swap(target_array, i, i-1)

    return target_array


def _search(ele, buffers):
    if ele < buffers[0]:
            return 0
    if ele >= buffers[-1]:
            return len(buffers)
    for idx in range(1, len(buffers)):
        if ele < buffers[idx] and ele >= buffers[idx - 1]:
            return idx


def naive_insert_sort(_arr):

    buffers = [_arr[0]]

    for ele in _arr[1:]:
        insert_idx = _search(ele, buffers)
        buffers.insert(insert_idx, ele)

    return buffers


def _binary_search(_arr, val, start, end):
    if end - start == 0:
        return start
    mid = (end + start) // 2
    if _arr[mid] == val:
        return mid
    elif _arr[mid] > val:
        return _binary_search(_arr, val, start, mid)
    else:
        return _binary_search(_arr, val, mid+1, end)


def binary_search_select_sort(_arr):
    buffers = [_arr[0]]

    for ele in _arr[1:]:
        insert_idx = _binary_search(buffers, ele, 0, len(buffers))
        buffers.insert(insert_idx, ele)

    return buffers


def _merge(a, b):
    m_arr = []
    while a and b:
        if a[0] <= b[0]:
            m_arr.append(a[0])
            a.pop(0)
        else:
            m_arr.append(b[0])
            b.pop(0)
    m_arr.extend(a)
    m_arr.extend(b)

    return m_arr


def merge_sort(target_arr):
    if len(target_arr) <= 1:
        return target_arr

    mid = len(target_arr) // 2

    return _merge(merge_sort(target_arr[:mid]), merge_sort(target_arr[mid:]))


class Heap:
    def __init__(self, nums):
        self._arr = nums

    def extract_min(self):
        min_val = self._arr[0]
        self.swap(0, len(self._arr)-1)
        self._arr.pop()
        if self._arr:
            self.shift_down(0)
        return min_val

    def get_min(self):
        return self._arr[0]

    def insert(self, x):
        self._arr.append(x)
        self.shift_up(len(self._arr) - 1)

    def shift_up(self, i):
        _parent = self.parent(i)
        if self._arr[i] < self._arr[_parent]:
            self.swap(i, _parent)
            if _parent > 0:
                self.shift_up(_parent)

    def shift_down(self, i):
        _left_child = self.left_child(i)
        _right_child = self.right_child(i)

        min_i = i
        min_val = self._arr[i]
        if _left_child < len(self._arr) and self._arr[_left_child] < min_val:
            min_val = self._arr[_left_child]
            min_i = _left_child
        if _right_child < len(self._arr) and self._arr[_right_child] < min_val:
            min_i = _right_child
        if i != min_i:
            self.swap(i, min_i)
            self.shift_down(min_i)

    def parent(self, i):
        a = i + 1
        return (a // 2) - 1

    def left_child(self, i):
        a = i + 1
        return (a * 2) - 1

    def right_child(self, i):
        a = i + 1
        return (a * 2 + 1) - 1

    def swap(self, i, j):
        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]


def heap_sort2(target_arr):
    heap = Heap([])
    for ele in target_arr:
        heap.insert(ele)
        # print "heap arr debug: ", heap._arr
    return [heap.extract_min() for _ in range(len(heap._arr))]


def heapify(target_arr, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and target_arr[l] > target_arr[smallest]:
        smallest = l
    if r < n and target_arr[r] > target_arr[smallest]:
        smallest = r

    if smallest != i:
        target_arr[i], target_arr[smallest] = target_arr[smallest], target_arr[i]
        heapify(target_arr, n, smallest)


def heap_sort3(target_arr):
    n = len(target_arr)

    # building the min-heap
    for i in range(n, -1, -1):
        heapify(target_arr, n, i)

    # print target_arr
    # heap sort
    for j in range(n-1, 0, -1):
        target_arr[0], target_arr[j] = target_arr[j], target_arr[0]
        heapify(target_arr, j, 0)


def heap_sort(target_arr):
    heapq.heapify(target_arr)

    result = [heapq.heappop(target_arr) for _ in range(len(target_arr))]

    return result


if __name__ == '__main__':
    ts_build_in = []
    ts_select_sort = []
    ts_naive_insert_sort = []
    ts_bubble_sort = []
    ts_binary_search_select_sort = []
    ts_quick_sort = []
    ts_quick_sort2 = []
    ts_merge_sort = []
    ts_heap_sort = []
    ts_heap_sort2 = []
    ts_heap_sort3 = []

    for _ in range(10):
        test_array = [random.randint(-1000, 1000) for _ in range(10)]

        tic = time.time()
        t1 = select_sort(copy.copy(test_array))
        ts_select_sort.append(time.time() - tic)

        tic = time.time()
        t2 = bubble_sort(copy.copy(test_array))
        ts_bubble_sort.append(time.time() - tic)

        tic = time.time()
        t3 = naive_insert_sort(copy.copy(test_array))
        ts_naive_insert_sort.append(time.time() - tic)

        tic = time.time()
        t4 = binary_search_select_sort(copy.copy(test_array))
        ts_binary_search_select_sort.append(time.time() - tic)

        tic = time.time()
        t5 = quick_sort(copy.copy(test_array))
        ts_quick_sort.append(time.time() - tic)

        tic = time.time()
        tt = copy.copy(test_array)
        t6 = quick_sort2(tt)
        ts_quick_sort2.append(time.time() - tic)

        tic = time.time()
        t7 = merge_sort(copy.copy(test_array))
        ts_merge_sort.append(time.time() - tic)

        tic = time.time()
        t8 = heap_sort(copy.copy(test_array))
        ts_heap_sort.append(time.time() - tic)

        tic = time.time()
        t9 = heap_sort2(copy.copy(test_array))
        ts_heap_sort2.append(time.time() - tic)

        tic = time.time()
        t10 = copy.copy(test_array)
        heap_sort3(t10)
        ts_heap_sort3.append(time.time() - tic)


        tic = time.time()
        test_array.sort()
        ts_build_in.append(time.time() - tic)

        print t1
        print t2
        print t3
        print t4
        print t5
        print t6
        print t7
        print t8
        print t9
        print t10
        print test_array
        assert t1 == t2 == t3 == t4 == t5 == t6 == t7 == t8 == t9 == t10 == test_array


    print "build in {}".format(np.mean(ts_build_in))
    print "ts_select_sort ",  np.mean(ts_select_sort)
    print "ts_naive_insert_sort ", np.mean(ts_naive_insert_sort)
    print "ts_bubble_sort ", np.mean(ts_bubble_sort)
    print "ts_binary_search_select_sort ", np.mean(ts_binary_search_select_sort)
    print "ts_quick_sort ", np.mean(ts_quick_sort)
    print "ts_quick_sort2 ", np.mean(ts_quick_sort2)
    print "ts_merge_sort ", np.mean(ts_merge_sort)
    print "ts_heap_sort ", np.mean(ts_heap_sort)
    print "ts_heap_sort2 ", np.mean(ts_heap_sort2)
    print "ts_heap_sort3 ", np.mean(ts_heap_sort3)

# build in 0.00326411724091
# ts_select_sort  3.02807388306
# ts_naive_insert_sort  2.06226789951
# ts_bubble_sort  11.229900074
# ts_binary_search_select_sort  0.0767011880875
# ts_quick_sort  0.0594287633896
# ts_quick_sort2  0.0848829984665
# ts_merge_sort  0.110533761978
# ts_heap_sort  0.0712699890137
