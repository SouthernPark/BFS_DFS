"""
Math 560
Project 2
Fall 2021

p2stack.py

Partner 1: QiangQiang Liu
Partner 2: Zelin Jin
Date: 11/01/2021
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        # The stack is full if the number of stored elements equals to the size of queue.
        if len(self.stack) == self.numElems:
            return True
        return False

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        if self.numElems == 0:
            return True
        return False

    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        # Declare a temp array of size 2 * numElems to store more elements.
        temp_arr = [None for x in range(0, 2 * self.numElems)]
        # Copy the elements in original array to the new temp array.
        for i in range(0, self.numElems):
            temp_arr[i] = self.stack[i]
        # Set the temp array as new array.
        self.stack = temp_arr
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        # If the stack is full, resize the stack.
        if self.isFull():
            self.resize()
        # Renew the parameters and store the number to the top of the stack
        self.top += 1
        self.numElems += 1
        self.stack[self.top] = val
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        if self.top < 0:
            return None
        self.top -= 1
        self.numElems -= 1
        # Return the target number on the top of the stack
        return self.stack[self.top + 1]