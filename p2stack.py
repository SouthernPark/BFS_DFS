"""
Math 560
Project 2
Fall 2021

p2stack.py

Partner 1:
Partner 2:
Date:
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
        # init the array for the stack
        self.stack = [None for x in range(0, size)]
        # index of the top element
        self.top = -1
        # numElems record how many elements have been put into stack
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
        # check if numElements is equal to len of the array
        if(self.numElems == len(self.stack)):
            return True
        return False

    """
    isEmpty function to check if the stack is empty.
    """

    def isEmpty(self):
        ##### IMPLEMENT! #####
        if(self.numElems == 0):
            return True
        return False

    """
    resize function to resize the stack by doubling its size.
    """

    def resize(self):
        ##### IMPLEMENT! #####
        temp = [None for i in range(len(self.stack)*2)]
        # copy the elements in stack to temp
        for i in range(self.numElems):
            temp[i] = self.stack[i]
        self.stack = temp
        return

    """
    push function to push a value onto the stack.
    """

    def push(self, val):
        ##### IMPLEMENT! #####
        # check whether the stack is full
        if(self.isFull()):
            self.resize()
        self.top += 1
        self.stack[self.top] = val
        self.numElems += 1
        return

    """
    pop function to pop the value off the top of the stack.
    """

    def pop(self):
        ##### IMPLEMENT! #####
        if(self.numElems == 0 or self.top < 0):
            return None

        res = self.stack[self.top]
        self.top -= 1
        self.numElems -= 1

        return res
