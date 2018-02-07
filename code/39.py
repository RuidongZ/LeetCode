# -*- Encoding:UTF-8 -*-

# 39. Combination Sum

# Given a set of candidate numbers (C) (without duplicates) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#     [7],
#     [2, 2, 3]
# ]


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.dfs(sorted(candidates), 0, [], target)
        return self.ans

    def dfs(self, candidates, idx, tmp, target):
        if sum(tmp) == target:
            self.ans.append(list(tmp))
            return False
        if sum(tmp) > target:
            return False

        for i in range(idx, len(candidates)):
            tmp.append(candidates[i])
            if not self.dfs(candidates, i, tmp, target):
                tmp.pop()
                return True
            tmp.pop()
        return True
