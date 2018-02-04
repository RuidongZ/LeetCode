# -*- Encoding:UTF-8 -*-

# 594. Longest Harmonious Subsequence

# We define a harmonious array is an array
# where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of
# its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ans = 0
        l = sorted(list(set(nums)))
        for i in range(len(l)-1):
            if l[i] + 1 in d:
                tmp = d[l[i]] + d[l[i+1]]
                if tmp > ans:
                    ans = tmp
        return ans
