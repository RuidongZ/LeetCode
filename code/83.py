# -*- Encoding:UTF-8 -*-

# 83. Remove Duplicates from Sorted List

# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            tmp = cur.next
            while tmp and cur.val == tmp.val:
                tmp = tmp.next
            cur.next = tmp
            cur = cur.next
        return head
