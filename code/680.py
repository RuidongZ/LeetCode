# -*- Encoding:UTF-8 -*-

# 680. Valid Palindrome II

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(int(len(s)//2)):
            if s[i] != s[len(s)-i-1]:
                return s[i+1:len(s)-i] == s[i+1:len(s)-i][::-1] or s[i:len(s)-i-1] == s[i:len(s)-i-1][::-1]
        return True
