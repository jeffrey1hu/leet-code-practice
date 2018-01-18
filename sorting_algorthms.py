import copy
import random
import heapq

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


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
    test_array = [5, 3, 1, 4, 5, 6, 8, 9, 2, 4, 5, 1, 11, 35]
    print "select_sort result: ", select_sort(copy.copy(test_array))
    print "bubble_sort result: ", bubble_sort(copy.copy(test_array))
    print "naive_insert_sort: ", naive_insert_sort(copy.copy(test_array))
    print "binary_search_select_sort: ", binary_search_select_sort(copy.copy(test_array))
    print "quick_sort result: ", quick_sort(copy.copy(test_array))
    print "merge_sort result: ", merge_sort(copy.copy(test_array))
    print "heap_sort result: ", heap_sort(copy.copy(test_array))