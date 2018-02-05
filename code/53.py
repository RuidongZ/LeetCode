# -*- Encoding:UTF-8 -*-

# 53. Maximum Subarray

# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        mx = -float("inf")

        for i in nums:
            sum = max(i, sum + i)
            mx = max(mx, sum)
        return mx
