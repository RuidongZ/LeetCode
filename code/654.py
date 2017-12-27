# -*- Encoding:UTF-8 -*-

# 654. Maximum Binary Tree
# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

#The root is the maximum number in the array.
#The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
#The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
#Construct the maximum tree by the given array and output the root node of this tree.

#Note:
#The size of the given array will be in the range [1,1000].

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        maxNum = max(nums)
        maxIdx = nums.index(maxNum)
        ans = TreeNode(maxNum)
        ans.left = self.constructMaximumBinaryTree(nums[:maxIdx])
        ans.right = self.constructMaximumBinaryTree(nums[maxIdx+1:])
        return ans