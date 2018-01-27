import time
import random
import numpy as np


def naive_array_median(target_array):
    target_array.sort()

    if len(target_array) % 2 == 0:
        mid = len(target_array) / 2
        return (target_array[mid-1] + target_array[mid]) / 2.
    else:
        mid = (len(target_array)+1) / 2
        return target_array[mid-1]


def array_media_divide_conquer(target_array):

    if len(target_array) % 2 == 0:
        mid = len(target_array) / 2
        return (_find_nth_digit(target_array, mid) + _find_nth_digit(target_array, mid+1)) / 2.
    else:
        mid = (len(target_array)+1) / 2
        return _find_nth_digit(target_array, mid)


def array_media_divide_conquer2(target_array):

    if len(target_array) % 2 == 0:
        mid = len(target_array) // 2
        mid_left = _nth_digit(target_array, mid, 0, len(target_array)-1)
        mid_right = _nth_digit(target_array, mid+1, 0, len(target_array)-1)
        return (mid_left + mid_right) / 2.0
    else:
        mid = (len(target_array)+1) // 2
        return _nth_digit(target_array, mid, 0, len(target_array)-1)


def _find_nth_digit(_arr, n):

    rd_idx = random.randint(0, len(_arr)-1)
    base_ele = _arr[rd_idx]
    larger = []
    smaller = []
    for k, ele in enumerate(_arr):
        if k == rd_idx:
            continue
        if ele > base_ele:
            larger.append(ele)
        else:
            smaller.append(ele)

    if len(smaller) == n - 1:
        return base_ele
    elif len(smaller) > n - 1:
        return _find_nth_digit(smaller, n)
    else:
        return _find_nth_digit(larger, n - len(smaller) - 1)

def _nth_digit(nums, n, start, end):

    base = random.randint(start, end)
    pivot = nums[base]

    nums[base], nums[start] = nums[start], nums[base]

    i = start
    j = end
    while j > i:
        while j > i and nums[j] > pivot:
            j -= 1
        nums[j], nums[i] = nums[i], nums[j]
        while j > i and nums[i] <= pivot:
            i += 1
        nums[i], nums[j] = nums[i], nums[j]

    if i - start > n - 1:
        return _nth_digit(nums, n, start, i-1)
    elif i - start == n - 1:
        # for double array median
        return nums[i]
    else:
        return _nth_digit(nums, n-i+start-1, i+1, end)



if __name__ == '__main__':
    ts1 = []
    ts2 = []
    ts3 = []
    for _ in range(1000):
        median = random.randint(-1000, 1000)
        l1 = [random.randint(median-1000, median-1) for _ in range(1000)]
        l2 = [random.randint(median+1, median+1000) for _ in range(1000)]
        test_arr = l1 + [median] + l2
        random.shuffle(test_arr)


        tic = time.time()
        r1 = naive_array_median(test_arr)
        toc1 = time.time()
        r2 =  array_media_divide_conquer(test_arr)
        toc2 = time.time()
        r3 = array_media_divide_conquer2(test_arr)
        toc3 = time.time()

        ts1.append(toc1 - tic)
        ts2.append(toc2 - toc1)
        ts3.append(toc3 - toc2)
        print "media {}, r1 {}, r2 {}, r3 {}".format(median, r1, r2, r3)
        assert r1 == r2 == median == r3
    print "naive algorithm time consume is %f" % np.mean(ts1)
    print "d&c algorithm time consume is %f" % np.mean(ts2)
    print "d&c algorithm 2 time consume is %f" % np.mean(ts3)

# A = [3,1,4,0,..]  # int32
#
# # time complexity
# 1 + 1/2 + 1/4 ....
#
#
# import random
# #topk
# def fn(A, k):
#     if len(A) <= k:
#         return A
#
#     kth_num = find_kth_num(A, k, 0, len(A)-1)
#
#     top_k = []
#     num_of_kth = 0
#
#     for num in A:
#         if num >= kth_num:
#             top_k.append(num)
#         #if num = kth_num:
#         #    num_of_kth += 1
#     #top_k.extend([kth_num] * (k-len(top_k)) )
#
#     return top_k
#
#
# def find_kth_num(nums, k, start, end):
#
#     rd_idx = random.randint(start, end)
#     pivot = nums[rd_idx]
#
#     i = start
#     j = end
#
#     swap(nums, i, rd_idx)
#
#     while j > i:
#         while j > i and nums[j] > num[pivot]:
#             j -= 1
#         swap(nums, i, j)
#         while j > i and num[i] <= num[pivot]:
#             i += 1
#         swap(nums, i, j)
#
#     if i - start > k - 1:
#         return find_kth_num(nums, k, start, i-1)
#     elif i - start == k - 1:
#         return nums[i]
#     else:
#         return find_kth_num(nums, k-i+start-1, i+1, end)
#
#
#
#
#
# def swap(nums, i, j):
#     nums[i], nums[j] = nums[j], num[i]
