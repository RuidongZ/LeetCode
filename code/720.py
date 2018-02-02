# -*- Encoding:UTF-8 -*-

# 720. Longest Word in Dictionary

# Given a list of strings words representing an English Dictionary,
# find the longest word in words that can be built one character at a time by other words in words.
# If there is more than one possible answer, return the longest word with the smallest lexicographical order.
#
# If there is no answer, return the empty string.
# Example 1:
# Input:
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation:
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation:
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
# Note:
#
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        d = {}
        for i in words:
            if len(i) in d:
                if i not in d[len(i)]:
                    d[len(i)].append(i)
            else:
                d[len(i)] = [i]

        i = 1
        tmp = d[i]
        while True:
            ans = []
            if i+1 in d:
                cmp = d[i+1]
            else:
                break
            for k in tmp:
                for j in cmp:
                    if k == j[:-1]:
                        ans.append(j)
            if not ans:
                break
            tmp = ans
            i += 1
        return sorted(tmp)[0]
