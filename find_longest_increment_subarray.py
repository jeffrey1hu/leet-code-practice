


test_arr = [1, -1, 2, -3, 4, -5, 6, -7]


def solution(target_array):
    max_length = 0
    for i in range(len(target_array)-1):
        last_digit = target_array[i]
        length = 1
        for ele in target_array[i+1:]:
            if ele > last_digit:
                last_digit = ele
                length += 1
        if length > max_length:
            max_length = length
    return max_length


if __name__ == '__main__':
    print solution(test_arr)
