# -*- Encoding:UTF-8 -*-

# 260. Single Number III

# Given an array of numbers nums, in which exactly two elements appear only once and
# all the other elements appear exactly twice. Find the two elements that appear only once.

# For example:
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant space complexity?


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # sort & traverse is STUPID way
        # USING XOR
        tmp = 0
        for i in nums:
            tmp ^= i

        n = tmp & ~(tmp-1)

        ans1 = 0
        ans2 = 0
        for i in nums:
            if n & i == 0:
                ans1 ^= i
            else:
                ans2 ^= i
        return [ans1, ans2]
