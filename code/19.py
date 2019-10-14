# -*- Encoding:UTF-8 -*-

# 19. Remove Nth Node From End of List

# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        while cur is not None and n != -1:
            cur = cur.next
            n -= 1

        if n == 0:
            return head.next

        ans = head
        while cur is not None:
            cur = cur.next
            ans = ans.next
        ans.next = ans.next.next
        return head
