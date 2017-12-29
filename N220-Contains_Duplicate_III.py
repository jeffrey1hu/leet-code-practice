class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in xrange(len(nums)):
            window_k_start = i
            window_k_end = i + k + 1
            cur_window = nums[window_k_start: window_k_end]
            for ij in range(len(cur_window)):
                for ik in range(ij+1, len(cur_window)):
                    if abs((cur_window[ij] - cur_window[ik])) <= t:
                        return True
        return False