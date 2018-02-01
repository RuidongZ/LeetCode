# -*- Encoding:UTF-8 -*-

# 137. Single Number II

# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return (3*sum(set(nums)) - sum(nums))/2
        one = 0
        two = 0
        three = 0
        for i in range(0, len(nums)):
            two |= one & nums[i]  # 当新来的为0时，two = two | 0，two不变，
            # 当新来的为1时，（当one此时为0，则two = two|0，two不变；当one此时为1时，则two = two | 1，two变为1
            one ^= nums[i]       # 新来的为0，one不变，新来为1时，one是0、1交替改变
            three = one & two    # 当one和two为1是，three为1（此时代表要把one和two清零了）
            one &= ~three        # 把one清0
            two &= ~three        # 把two清0
        return one
