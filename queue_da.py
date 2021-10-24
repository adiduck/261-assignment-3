# Name: Alexandra Diduck
# OSU Email: diducka@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 10/18/21
# Description:
# Description:

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self):
        """
        Return content of stack in human-rea_dable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """Adds a new value at the end of the queue. Implemented with O(1) amortized runtime complexity."""

        self._da.append(value)

    def dequeue(self) -> object:
        """Removes and returns the value from the beginning of the queue. If the queue is empty, the method
        raises a QueueException. Implemented with O(N) runtime complexity."""

        # If the queue is empty, raises exception.
        if self._da.is_empty():
            raise QueueException

        # Must get value before removal, calls get_at_index method to return the element from the start of the queue.
        start_element = self._da.get_at_index(0)
        # Calls remove_at_index method to remove the element from the top.
        self._da.remove_at_index(0)

        # Returns the element from the top of the stack that was removed.
        return start_element


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)


    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
