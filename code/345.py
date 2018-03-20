# -*- Encoding:UTF-8 -*-

# 345. Reverse Vowels of a String

# Write a function that takes a string as input and reverse only the vowels of a string.
# 
# Example 1:
# Given s = "hello", return "holle".
# 
# Example 2:
# Given s = "leetcode", return "leotcede".


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow_set = set("aeiouAEIOU")

        vowels = []
        idx = []
        ans = []
        for i, c in enumerate(s):
            ans.append(c)
            if c in vow_set:
                vowels.append(c)
                idx.append(i)

        vowels.reverse()

        for i, index in enumerate(idx):
            ans[index] = vowels[i]
        return "".join(ans)
