# -*- Encoding:UTF-8 -*-

# 560. Subarray Sum Equals K

# Given an array of integers and an integer k, you need to find the total number of continuous subarrays
# whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hs = {0: 1}
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in hs:
                count += hs[sum - k]
            if sum in hs:
                hs[sum] += 1
            else:
                hs[sum] = 1
        return count
        '''
        ans = 0
        d = {0: [-1]}
        tmp = 0
        for i, n in enumerate(nums):
            tmp += n
            if tmp in d:
                d[tmp].append(i)
            else:
                d[tmp] = [i]

        for key in d:
            tmp = k+key
            if tmp in d:
                for i in d[key]:
                    for j in d[tmp]:
                        if j > i:
                            ans += 1
        return ans
        '''
