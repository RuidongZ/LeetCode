# -*- Encoding:UTF-8 -*-

# 416. Partition Equal Subset Sum

# Given a non-empty array containing only positive integers, find if the array can be partitioned
# into two subsets such that the sum of elements in both subsets is equal.
#
# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Better Way
        s = sum(nums)
        if s & 1 == 1:
            return False
        s = 1 << int(s/2)
        recorder = 1
        nums.sort(reverse=True)
        for n in nums:
            recorder |= recorder << n
            if s & recorder:
                return True
        return False
        '''
        def helper(start, target):
            if target < 0:
                return False
            elif target == 0:
                return True
            for i in range(start, len(nums)):
                if helper(i+1, target-nums[i]):
                    return True
            return False

        nums = sorted(nums, reverse=True)
        total = sum(nums)
        if total % 2 != 0:
            return False
        else:
            exp = total // 2

        return helper(0, exp)
        '''