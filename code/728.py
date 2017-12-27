# -*- Encoding:UTF-8 -*-

# 728. Self Dividing Numbers
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self dividing number,
# including the bounds if possible.

# Input: left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# The boundaries of each input argument are 1 <= left <= right <= 10000.

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for i in range(left, right+1):
            strNum = str(i)
            if not isContainZero(strNum):
                flag = 0
                for j in strNum:
                    if i % int(j) != 0:
                        flag = 1
                        break
                if flag == 0:
                    ans.append(i)
        return ans


def isContainZero(num):
    s = set(num)
    if '0' in s:
        return True
    else:
        return False

if __name__ == '__main__':
    sol = Solution()
    ans = sol.selfDividingNumbers(1, 22)
    print(ans)