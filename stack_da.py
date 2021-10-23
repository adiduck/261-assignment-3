# Name: Alexandra Diduck
# OSU Email: diducka@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 10/25/2021
# Description: Implements a Stack ADT class that uses the Dynamic Array data structure as the
# underlying data storage.

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da_val = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da_val.length()) + " elements. ["
        out += ', '.join([str(self._da_val[i]) for i in range(self._da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """Adds a new element to the top of the stack. It must be implemented in O(1) amortized runtime
        complexity."""

        # Adds the element to the 'end'/top of the stack.
        self._da_val.append(value)

    def pop(self) -> object:
        """Removes the top element from the stack and returns its value. Implemented in O(1) amortized
        runtime complexity. If the stack is empty, raises a custom StackException."""

        # If the stack is empty, raises exception.
        if self._da_val.is_empty():
            raise StackException

        # Must get value before removal, calls get_at_index method to return the element from the top of the stack.
        top_element = self._da_val.get_at_index(self.size()-1)
        # Calls remove_at_index method to remove the element from the top.
        self._da_val.remove_at_index(self.size() - 1)

        # Returns the element from the top of the stack that was removed.
        return top_element

    def top(self) -> object:
        """Returns the value from the top element of the stack without removing it. It must be implemented
        with O(1) runtime complexity. If the stack is empty, the method raises a custom StackException."""

        # If the stack is empty, raises exception.
        if self._da_val.is_empty():
            raise StackException

        # Calls the get_at_index method to return the element from the top of the stack.
        return self._da_val.get_at_index(self.size()-1)

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
