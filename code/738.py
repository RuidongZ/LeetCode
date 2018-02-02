# -*- Encoding:UTF-8 -*-

# 738. Monotone Increasing Digits

# Given a non-negative integer N, find the largest number
# that is less than or equal to N with monotone increasing digits.
#
# (Recall that an integer has monotone increasing digits
# if and only if each pair of adjacent digits x and y satisfy x <= y.)
#
# Example 1:
# Input: N = 10
# Output: 9
# Example 2:
# Input: N = 1234
# Output: 1234
# Example 3:
# Input: N = 332
# Output: 299
# Note: N is an integer in the range [0, 10^9].


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = str(N)
        ans = []
        for i in range(len(s)-1):
            if s[i+1] >= s[i]:
                ans.append(s[i])
            else:
                tmp = int(s[i])-1
                while ans:
                    if tmp >= int(ans[-1]):
                        break
                    else:
                        tmp = int(ans.pop())-1
                ans.append(str(tmp))
                for _ in range(len(s) - len(ans)):
                    ans.append("9")
                return int("".join(ans))
        ans.append(s[-1])
        return int("".join(ans))

sol = Solution()
ans = sol.monotoneIncreasingDigits(10)
print(ans)