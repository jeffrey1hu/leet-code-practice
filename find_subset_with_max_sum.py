import numpy as np

# DP
def find_maximum_subset_dp(target_arr):
    start_max = [None] * len(target_arr)
    all_max = [None] * len(target_arr)

    start_max[-1] = target_arr[-1]
    all_max[-1] = target_arr[-1]

    for i in range(len(target_arr)-2, -1, -1):
        start_max[i] = max(start_max[i+1]+target_arr[i], target_arr[i])
        all_max[i] = max(all_max[i+1], start_max[i])
    return all_max[0]

def find_maximum_subset_dp_improved(target_arr):

    last_start_max = target_arr[-1]
    last_all_max = target_arr[-1]

    start_pointer = len(target_arr) - 1

    for i in range(len(target_arr)-2, -1, -1):
        last_start_max = max(last_start_max+target_arr[i], target_arr[i])

        if last_start_max > last_all_max:
            start_pointer = i

        last_all_max = max(last_all_max, last_start_max)

    temp_sum = 0
    for i in range(start_pointer, len(target_arr)):
        temp_sum += target_arr[i]
        if temp_sum == last_all_max:
            end_pointer = i
            break

    return start_pointer, end_pointer, last_all_max

# Divide and conquer

def find_maximum_subset(target_arr, start, end):
    if end - start == 1:
        return start, end, target_arr[start]
    if end - start == 0:
        return start, end, 0

    mid = (end + start) // 2
    # print("target_arr {}, start {}, end {}, mid {}".format(target_arr, start, end, mid))

    start_left, end_left, max_val_left = find_maximum_subset(target_arr, start, mid)
    start_right, end_right, max_val_right = find_maximum_subset(target_arr, mid, end)

    if max_val_left > max_val_right:
        start_idx = start_left
        bias_sum = np.sum(target_arr[end_left: end_right])
        if bias_sum > 0:
            end_idx = end_right
        else:
            end_idx = end_left
    else:
        end_idx = end_right
        bias_sum = np.sum(target_arr[start_left: start_right])
        if bias_sum > 0:
            start_idx = start_left
        else:
            start_idx = start_right

    if bias_sum > 0:
        max_sum = max(max_val_left, max_val_right) + bias_sum
    else:
        max_sum = max(max_val_left, max_val_right)

    return start_idx, end_idx, max_sum

if __name__ == '__main__':
    test_arr = [1, -4, 4, 5, 6, 10, -1, -5]
    start, end, result1 = find_maximum_subset(test_arr, 0, len(test_arr))
    print start, end-1, result1
    result2 = find_maximum_subset_dp(test_arr)
    print result2
    start1, end1, result3 = find_maximum_subset_dp_improved(test_arr)
    print start1, end1, result3
