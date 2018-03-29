# -*- Encoding:UTF-8 -*-

# 24. Swap Nodes in Pairs

# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. You may not modify the values in the list,
# only nodes itself can be changed.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        if not head.next:
            return head

        cur = head
        if cur and cur.next:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = cur
            newhead = tmp

        pre = cur
        cur = cur.next
        while cur and cur.next:
            pre.next = cur.next
            tmp = cur.next.next
            cur.next.next = cur
            cur.next = tmp

            pre = cur
            cur = cur.next

        return newhead
