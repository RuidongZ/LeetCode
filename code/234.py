# -*- Encoding:UTF-8 -*-

# 234. Palindrome Linked List

# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # odd
        if fast:
            slow = slow.next

        pre = None
        while slow:
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp

        tmp = head
        slow = slow.next
        while slow:
            if tmp.val != slow.val:
                return False
            tmp = tmp.next
            slow = slow.next
        return True
