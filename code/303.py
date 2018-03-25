# -*- Encoding:UTF-8 -*-

# 303. Range Sum Query - Immutable

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        total = 0
        self.nums = []
        for i in nums:
            total += i
            self.nums.append(total)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j] if i == 0 else self.nums[j] - self.nums[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
