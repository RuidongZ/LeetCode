# -*- Encoding:UTF-8 -*-

# 90. Subsets II

# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,2], a solution is:
#
# [
#     [2],
#     [1],
#     [1,2,2],
#     [2,2],
#     [1,2],
#     []
# ]


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        nums = sorted(nums)

        s = set()
        for i in nums:
            tmp = list(ans)
            for j in tmp:
                if tuple(j+[i]) not in s:
                    ans.append(j+[i])
                    s.add(tuple(j+[i]))
        return ans
