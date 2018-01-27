

def binary_search_recur(nums, val):
    return _binary_search_recur(nums, val, 0, len(nums)-1)


# Recursive
def _binary_search_recur(nums, val, start, end):
    if end - start < 0:
        return start

    mid = start + (end - start) // 2

    if val > nums[mid]:
        return _binary_search_recur(nums, val, mid+1, end)
    elif val < nums[mid]:
        return _binary_search_recur(nums, val, start, mid-1)
    else:
        return mid

def binary_search_iter(nums, val):
    return _binary_search_iter(nums, val, 0, len(nums)-1)

# Iterative
def _binary_search_iter(nums, val, start, end):

    while end >= start:

        mid = start + (end - start) // 2

        if val > nums[mid]:
            start = mid + 1
        elif val < nums[mid]:
            end = mid - 1
        else:
            return mid

    return start

def binary_search_largest_vaild(nums, val):
    return _binary_search_iter2(nums, val , 0, len(nums))


def _binary_search_iter2(nums, val, start, end):
    # print("start {}, end {}".format(start, end))
    while end > start+1:
        mid = start + (end - start) // 2

        if val >= nums[mid]:
            start = mid
        else:
            end = mid

        # print("start {}, end {}".format(start, end))

    if nums[start] == val:
        return start
    else:
        return -1



if __name__ == '__main__':
    tt = [1, 3, 5, 5, 7, 9]
    print binary_search_recur(tt, 6)
    print binary_search_iter(tt, 6)
    print binary_search_largest_vaild(tt, 6)
    tt.insert(4, 6)
    print tt







#
# def binary_search_insert(nums, val):
#
#     return _binary_search_insert_util(nums, val, 0, len(nums))
#
#
# def _binary_search_insert_util(nums, val, start, end):
#     if end - start == 0:
#         return start
#
#     mid = start + (end-start) // 2
#
#     if val > nums[mid]:
#         _binary_search_insert_util(nums, val, mid+1, end)
#     elif val < nums[mid]:
#         _binary_search_insert_util(nums, val, start, mid)
#     else:
#         return mid
