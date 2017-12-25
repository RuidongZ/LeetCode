class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        pre = 0
        temp = 0
        res = 0
        for i in s:
            cur = d[i]
            if cur == pre:
                temp += cur
            elif cur > pre:
                temp = cur - temp
            else:
                res += temp
                temp = cur

            pre = cur

        res += temp
        return res

if __name__ == '__main__':
    sol = Solution()
    ans = sol.romanToInt("MDCCCLXXXIV")
    print(ans)
