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


def quick_sort2(nums, start, end):
    # print("target sub array {}".format(nums[start: end+1]))
    if end - start <= 0:
        return
    idx = random.randint(start, end)
    pivot = nums[idx]
    swap(nums, idx, start)
    # print("pivot", pivot)
    i = start
    j = end

    while j > i:

        while nums[j] > pivot and j > i:
            j -= 1
        swap(nums, i, j)
        while nums[i] <= pivot and j > i:
            i += 1
        swap(nums, i, j)
        # print nums

    quick_sort2(nums, start, i-1)
    quick_sort2(nums, i+1, end)



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

    for _ in range(1000):
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
        quick_sort2(tt, 0, len(tt)-1)
        t6 = tt
        ts_quick_sort2.append(time.time() - tic)

        tic = time.time()
        t7 = merge_sort(copy.copy(test_array))
        ts_merge_sort.append(time.time() - tic)

        tic = time.time()
        t8 = heap_sort(copy.copy(test_array))
        ts_heap_sort.append(time.time() - tic)

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
        print test_array
        assert t1 == t2 == t3 == t4 == t5 == t6 == t7 == t8 == test_array


    print "build in {}".format(np.mean(ts_build_in))
    print "ts_select_sort ",  np.mean(ts_select_sort)
    print "ts_naive_insert_sort ", np.mean(ts_naive_insert_sort)
    print "ts_bubble_sort ", np.mean(ts_bubble_sort)
    print "ts_binary_search_select_sort ", np.mean(ts_binary_search_select_sort)
    print "ts_quick_sort ", np.mean(ts_quick_sort)
    print "ts_quick_sort2 ", np.mean(ts_quick_sort2)
    print "ts_merge_sort ", np.mean(ts_merge_sort)
    print "ts_heap_sort ", np.mean(ts_heap_sort)

# build in 0.00326411724091
# ts_select_sort  3.02807388306
# ts_naive_insert_sort  2.06226789951
# ts_bubble_sort  11.229900074
# ts_binary_search_select_sort  0.0767011880875
# ts_quick_sort  0.0594287633896
# ts_quick_sort2  0.0848829984665
# ts_merge_sort  0.110533761978
# ts_heap_sort  0.0712699890137
