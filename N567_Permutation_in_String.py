class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        target_count_arr = self.gen_count_arr(s1)
        substring_count_arr = self.gen_count_arr(s2[:len(s1)])
        same_freq_count = self.count_same_freq(target_count_arr, substring_count_arr)
        if same_freq_count == 26:
            return True
        for i in range(1, len(s2)-len(s1)+1):
            previous_char = self.char_idx(s2[i-1])
            recent_char = self.char_idx(s2[i+len(s1)-1])

            if target_count_arr[previous_char] == substring_count_arr[previous_char]:
                same_freq_count -= 1
            substring_count_arr[previous_char] -= 1
            if target_count_arr[previous_char] == substring_count_arr[previous_char]:
                same_freq_count += 1

            if target_count_arr[recent_char] == substring_count_arr[recent_char]:
                same_freq_count -= 1
            substring_count_arr[recent_char] += 1
            if target_count_arr[recent_char] == substring_count_arr[recent_char]:
                same_freq_count += 1

            if same_freq_count == 26:
                return True

        return False

    def gen_count_arr(self, s):
        count_arr = [0] * 26
        for _char in s:
            idx = self.char_idx(_char)
            count_arr[idx] += 1
        return count_arr

    def char_idx(self, char):
        return ord(char) - ord('a')

    def count_same_freq(self, arr1, arr2):
        counter = 0
        for i in range (len(arr1)):
            if arr1[i] == arr2[i]:
                counter += 1
        return counter

