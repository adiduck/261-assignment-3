# Name: Alexandra Diduck
# OSU Email: diducka@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 10/25/2021
# Description: Implements the Deque and Bag ADT interfaces with a Singly Linked List data structure.


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self._next = None
        self._value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)
        self._tail = SLNode(None)
        self._head._next = self._tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self._head._next != self._tail:
            cur = self._head._next._next
            out = out + str(self._head._next._value)
            while cur != self._tail:
                out = out + ' -> ' + str(cur._value)
                cur = cur._next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self._head
        while cur._next != self._tail:
            cur = cur._next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head._next == self._tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """Method adds a new node at the beginning of the list (right after the front sentinel)."""

        # Creates a new node with the passed value.
        new_node = SLNode(value)

        new_node._next = self._head._next
        self._head._next = new_node

    def add_back(self, value: object) -> None:
        """Method adds a new node at the end of the list (right before the sentinel)."""

        # Travels the list, starting at the head.
        cur = self._head

        # Iterates through the list and updates the current node till we reach the right position,
        # right before the tail.
        while cur._next != self._tail:
            # Progresses pointer.
            cur = cur._next

        # Creates a new node.
        new_node = SLNode(value)
        # Points new node's next to the tail.
        new_node._next = cur._next
        # Makes the new node the last node in the linked list, before the tail.
        cur._next = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """Adds a new value at the specified index position in the linked list. If the provided index is invalid,
        the method raises a custom SLLException."""

        if index < 0 or index > self.length():
            raise SLLException

        # Travel pointer initialized to head
        cur = self._head
        # Integer counter to count how many times the travel pointer goes
        # to the next chain.
        count = 0

        # Iterates through the list and updates the current node till we reach the right position,
        # where the counter equals the index.
        while count != index:
            # Progresses pointer.
            cur = cur._next
            count += 1

        new_node = SLNode(value)
        # Re-points and adds the new node.
        new_node._next = cur._next
        cur._next = new_node

    def remove_front(self) -> None:
        """Removes the first node from the list. If the list is empty, the method raises a SLLException."""

        # Raises exception if empty.
        if self.is_empty():
            raise SLLException

        # Re-points to 'remove' by 'skipping' over node.
        self._head._next = self._head._next._next

    def remove_back(self) -> None:
        """Removes the last node from the list. If the list is empty, the method raises a custom SLLException."""

        # Raises exception if empty.
        if self.is_empty():
            raise SLLException

        cur = self._head

        # Iterates through list to get to position before the tail node.
        while cur._next._next != self._tail:
            # Progresses pointer.
            cur = cur._next
        # Updates pointer.
        cur._next = self._tail

    def remove_at_index(self, index: int) -> None:
        """Method removes a node from the list given its index. If the provided index is invalid, the method
        raises a custom SLLException."""

        # Invalid conditions:
        if self.is_empty() or index < 0 or index > self.length() - 1:
            raise SLLException

        # Initializes count.
        count = 0
        cur = self._head

        # Iterates through the list and progresses node till condition is met, where we get to the given index.
        while count != index:
            cur = cur._next
            count += 1
        # Updates pointers.
        cur._next = cur._next._next

    def get_front(self) -> object:
        """Method returns the value from the first node in the list without removing it. If the list is empty,
        method raises a SLLException."""

        # Raises exception if empty.
        if self.is_empty():
            raise SLLException

        # Returns the value at the first node.
        return self._head._next._value

    def get_back(self) -> object:
        """Returns the value from the last node in the list without removing it. If the list is empty, the
        method raises a SLLException."""

        if self.is_empty():
            raise SLLException

        cur = self._head

        # Iterates through list and updates travel node till position before the tail is reached.
        while cur._next != self._tail:
            cur = cur._next
        # Returns the value at the travel node/right before sentinel.
        return cur._value

    def remove(self, value: object) -> bool:
        """Traverses the list from the beginning to the end and removes the first node in the list that matches
        the provided "value" object. Returns True if some node was actually removed from the list. Otherwise,
        returns False."""

        cur = self._head
        # Traverses list and updates traveler till the value of the node matches the passed object.
        while cur != self._tail and cur._next._value != value:
            cur = cur._next

        # If its empty or contains the value None, we can just return False as there's nothing to remove.
        if cur._next == None or self.is_empty():
            return False
        else:
            # Removes the node that matches the passed value by 'skipping' over it.
            cur._next = cur._next._next
            return True

    def count(self, value: object) -> int:
        """Method counts the number of elements in the list that match the provided "value" object."""

        # If its empty, there is nothing to count, returns 0.
        if self.is_empty():
            return 0

        # Initializes count to 0.
        count = 0

        # Don't count head (or tail).
        cur = self._head._next

        # Iterates through list till end:
        while cur != self._tail:
            # If the values match, increment the count by 1.
            if cur._value == value:
                count += 1
            # Progress the node.
            cur = cur._next
        # Returns the count after traversing the entire list.
        return count

    def slice(self, start_index: int, size: int) -> object:
        """Method returns a new LinkedList object that contains the requested number of nodes from the original list
        starting with the node located at the requested start index. If the provided start index is invalid or
        if there are not enough nodes between the start index and the end of the list to make a slice of the
        requested size, this method raises a custom “SLLException”.Implemented in O(N) runtime."""

        # Conditions:
        if size < 0:
            raise SLLException
        if start_index < 0:
            raise SLLException
        if (start_index + size - 1) >= self.length():
            raise SLLException
        if start_index >= self.length():
            raise SLLException

        # Creates a new linked list object.
        new_ll = LinkedList()
        # Initializes 'current' index to 0.
        cur_index = 0
        cur = self._head._next

        while cur_index != (start_index + size):
            # When we get to the point where we hit the start index, we can then add those nodes at those indexes
            # that fall within that given size to the new linked list object.
            if start_index <= cur_index < (start_index + size):
                # Calls add_back method to add a new node at the end of the list.
                new_ll.add_back(cur._value)
            # Progresses index.
            cur_index += 1
            # Progresses node.
            cur = cur._next
        # Returns the object.
        return new_ll

if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)


    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)


    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))


    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))


    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    # print(list)
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)


    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)


    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))


    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())


    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)


    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")


    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

