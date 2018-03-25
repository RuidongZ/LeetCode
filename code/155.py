# -*- Encoding:UTF-8 -*-

# 155. Min Stack

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

import sys


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxsize  # sys.maxint for python2

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.min = min(x, self.min)

    def pop(self):
        """
        :rtype: void
        """
        tmp = self.stack.pop()
        if tmp == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = sys.maxsize  # sys.maxint for python2

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
