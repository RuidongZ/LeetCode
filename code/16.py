# -*- Encoding:UTF-8 -*-

# 16. 3Sum Closest

# Given an array nums of n integers and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])

        for left in range(len(nums)-2):
            right = len(nums)-1
            cur = left + 1
            while cur < right:
                close_sum = nums[left] + nums[cur] + nums[right]

                if close_sum == target:
                    return close_sum

                if abs(close_sum - target) < abs(ans - target):
                    ans = close_sum

                if close_sum < target:
                    cur += 1
                elif close_sum > target:
                    right -= 1
                else:
                    break
        return ans
