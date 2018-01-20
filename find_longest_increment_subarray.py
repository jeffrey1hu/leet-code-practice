


# test_arr = [1, -1, 2, -3, 4, -5, 6, -7]


def solution_dp(target_array):
    max_values = []

    max_values.append(target_array[0])

    for i in range(1, len(target_array)):
        # print("max_values", max_values)
        for j in range(len(max_values)-1, -1, -1):
            if target_array[i] > max_values[j]:
                incr_length = j + 1
                if incr_length == len(max_values):
                    max_values.append(target_array[i])
                else:
                    if max_values[incr_length] > target_array[i]:
                        max_values[incr_length] = target_array[i]
                break
            if j == 0:
                if max_values[0] > target_array[i]:
                    max_values[0] = target_array[i]

    return len(max_values)

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


def solution_dp_improve(target_array):
    max_values = []

    max_values.append(target_array[0])

    for i in range(1, len(target_array)):
        # print("max_values", max_values)

        j = _binary_search(max_values, target_array[i], 0, len(max_values))
        if j == len(max_values):
            max_values.append(target_array[i])
        elif target_array[i] < max_values[j]:
            max_values[j] = target_array[i]
        else:
            continue

    return len(max_values)

if __name__ == '__main__':
    import random
    for _ in range(1000):
        # print(_)
        length = random.randint(5, 10)
        test_arr = [random.randint(-1000, 1000) for _ in xrange(length)]
        # print test_arr
        a =  solution_dp(test_arr)
        b = solution_dp_improve(test_arr)
        print a, b
        assert a == b, "a {}, b {}".format(a, b)