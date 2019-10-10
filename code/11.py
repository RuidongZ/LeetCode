# -*- Encoding:UTF-8 -*-

# 11. Container With Most Water

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.
#
# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ans = 0
        while left < right:
            ans = max(min(height[left], height[right])*(right-left), ans)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return ans
