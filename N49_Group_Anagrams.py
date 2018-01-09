class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for _str in strs:
            count_arr = [0] * 26
            for _char in _str:
                idx = ord(_char) - ord('a')
                count_arr[idx] += 1
            _count_tuple = tuple(count_arr)
            result.setdefault(_count_tuple, [])
            result[_count_tuple].append(_str)
        return result.values()