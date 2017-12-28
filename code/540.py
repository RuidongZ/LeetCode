# -*- Encoding:UTF-8 -*-

# 540. Single Element in a Sorted Array

# Given a sorted array consisting of only integers where every element appears twice
# except for one element which appears once. Find this single element that appears only once.

# Example 1:
# Input: [1,1,3,3,4,4,2,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        idx = len(nums)//2
        cnt = (len(nums)-1)//2
        if nums[idx] == nums[idx-1]:
            if cnt % 2 == 0:
                ans = self.singleNonDuplicate(nums[:idx+1])
            else:
                ans = self.singleNonDuplicate(nums[idx+1:])
        elif nums[idx] == nums[idx+1]:
            if cnt % 2 == 0:
                ans = self.singleNonDuplicate(nums[idx:])
            else:
                ans = self.singleNonDuplicate(nums[:idx])
        else:
            return nums[idx]
        return ans
