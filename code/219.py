# -*- Encoding:UTF-8 -*-

# 219. Contains Duplicate II

# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}

        for i, n in enumerate(nums):
            if n in d and i - d[n] <= k:
                    return True
            else:
                d[n] = i
        return False
