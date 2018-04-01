# -*- Encoding:UTF-8 -*-

# 75. Sort Colors

# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if sum(nums[i:]) == 2 * len(nums[i:]):
                return
            if nums[i] == 0:
                nums.insert(0, nums.pop(i))
            elif nums[i] == 2:
                nums.insert(len(nums), nums.pop(i))
                continue
            i += 1
