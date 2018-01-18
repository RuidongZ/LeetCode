# -*- Encoding:UTF-8 -*-

# 216. Combination Sum III

# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
#
# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        if (19-k)*k/2 < n:
            return ans
        nums = list(range(1, 10))
        self.dfs(nums, k, n, ans, [])
        return ans

    def dfs(self, nums, k, n, ans, tmp):
        if n == 0 and len(tmp) == k:
            ans.append(list(tmp))
            return
        for i, x in enumerate(nums):
            if x <= n:
                tmp.append(x)
                self.dfs(nums[i+1:], k, n-x, ans, tmp)
                tmp.pop()
