# -*- Encoding:UTF-8 -*-

# 445. Add Two Numbers II

# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = l1
        a = ""
        while h:
            a += str(h.val)
            h = h.next
        h = l2
        b = ""
        while h:
            b += str(h.val)
            h = h.next
        c = str(int(a)+int(b)) # 超出int表示范围 -- 字符串处理或者用栈
        ans = ListNode(c[0])
        cur = ans
        for i in c[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return ans
