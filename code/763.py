# -*- Encoding:UTF-8 -*-

# 763. Partition Labels

# A string S of lowercase letters is given. We want to partition this string into as many parts as possible
# so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
#
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        d = {}
        for i, s in enumerate(S):
            if s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        tmp = []
        for key in d:
            start, end = d[key][0], d[key][-1]
            tmp.append([start, end])
        tmp = sorted(tmp, key=lambda x: x[0])
        tmp_ans = tmp[0]
        i = 1
        while i < len(tmp):
            if tmp[i][0] in range(tmp_ans[0], tmp_ans[1]):
                if tmp[i][1] > tmp_ans[1]:
                    tmp_ans[1] = tmp[i][1]
            else:
                ans.append(len(S[tmp_ans[0]:tmp_ans[1]+1]))
                tmp_ans = [tmp[i][0], tmp[i][1]]
            i += 1
        ans.append(len(S[tmp_ans[0]:tmp_ans[1]+1]))
        return ans
