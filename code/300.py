# -*- Encoding:UTF-8 -*-

# 300. Longest Increasing Subsequence

# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
# Note that there may be more than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # Better Way
        from bisect import bisect_left
        stack = []
        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                stack[bisect_left(stack, num)] = num
        return len(stack)
        '''
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0:
                if nums[i] > nums[j] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
                j -= 1
        return max(dp)
