# -*- Encoding:UTF-8 -*-

# 78. Subsets

# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,3], a solution is:
#
# [
#     [3],
#     [1],
#     [2],
#     [1,2,3],
#     [1,3],
#     [2,3],
#     [1,2],
#     []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res
        """
        self.ans = []
        self.nums = sorted(nums)

        length = len(nums)
        idxs = [0] * length

        for i in range(0, length//2+1):
            self.dfs(idxs, 0, i)
        return self.ans

    def dfs(self, idxs, idx, num):
        if num == 0:
            self.idx2ans(idxs)
            return
        end = len(idxs)//2 if len(idxs) % 2 == 0 and num == len(idxs)//2 else len(idxs)-num+1
        for i in range(idx, end):
            idxs[i] = 1
            self.dfs(idxs, i+1, num-1)
            idxs[i] = 0

    def idx2ans(self, idx):
        tmp1 = []
        tmp2 = []
        for i, n in enumerate(idx):
            if n == 0:
                tmp1.append(self.nums[i])
            else:
                tmp2.append(self.nums[i])
        self.ans.append(tmp1)
        self.ans.append(tmp2)
        """
