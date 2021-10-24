# Name: Alexandra Diduck
# OSU Email: diducka@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 10/25/21
# Description: Implements a DynamicArray class. The DynamicArray class uses the StaticArray object as its
# underlying data storage container and provides methods.

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:

        """Changes the capacity of the underlying storage for the array element. The method should only accept positive
        integers for new_capacity. Additionally, new_capacity cannot be smaller than the number of elements
        currently stored in the dynamic array (which is tracked by the self.size variable). If new_capacity is not
        a positive integer or if new_capacity < self.size, this method should not do any work and immediately exit.
        Does not return anything."""

        # Exits if new_capacity is a negative integer or the new_capacity is less than the current size.
        if new_capacity <= 0 or new_capacity < self.size:
            return

        # Creates a new array with the given capacity.
        temp_array = StaticArray(new_capacity)
        # Iterates through the array to copy the value at the current index (i) from that array to the temp_array.
        for i in range(self.size):
            temp_array[i] = self.data[i]
        # Updates underlying data storage.
        self.data = temp_array
        # Updates the underlying capacity to the new_capacity.
        self.capacity = new_capacity

    def append(self, value: object) -> None:

        """Adds a new element at the end of the dynamic array. If the storage is full, doubles its capacity
         before adding a new value by calling resize method. Does not return anything."""

        # Checks if the storage is full (before adding a new value) and calls resize method to double capacity.
        if self.size >= self.capacity:
            self.resize(self.capacity * 2)
        # Adds value to the array.
        self.data[self.size] = value
        # Increments the size by one when a value is added.
        self.size += 1

    def insert_at_index(self, index: int, value: object) -> None:

        """Adds a new value at the specified index position in the dynamic array. If the provided index is invalid,
        raises a "DynamicArrayException." If the storage is full, doubles its capacity by calling resize method.
        Does not return anything."""

        # If the index is invalid, raises custom exception.
        if index < 0 or index > self.length():
            raise DynamicArrayException

        # If the storage is full, doubles the capacity by calling resize method.
        if self.size >= self.capacity:
            self.resize(self.capacity * 2)

        for i in range(self.length(), index, -1):
            self.data[i] = self.data[i - 1]

        # Adds value to the array.
        self.data[index] = value
        # Increments the size by one when a value is added.
        self.size += 1

    def remove_at_index(self, index: int) -> None:

        """Removes an element at the specified index from the dynamic array. If the provided index is invalid,
        raises a "DynamicArrayException." Capacity restrictions/changes must be made before removal of element(s):
        1.) When the number of elements stored in the array (before removal) is strictly less than 1/4 of its
        current capacity, the capacity must be reduced to twice the number of current elements.
        2.) If the current capacity (before reduction), is 10 elements or less, reduction does not occur.
        3.) If the current capacity (before reduction), is greater than 10 elements, the reduced capacity cannot
        become less than 10 elements.
        Does not return anything."""

        # Checks that index is valid:
        if index < 0 or index >= self.length():
            raise DynamicArrayException

        # Condition 2:
        if self.capacity <= 10:
            self.capacity = self.capacity
        # Capacity adjustments must be made before removal:
        else:
            # Condition 1:
            if self.size < (self.capacity * (1/4)) and self.size * 2 >= 10:
                self.resize(self.size * 2)
            # Condition 3:
            elif self.size < (self.capacity * (1/4)) and self.size * 2 < 10:
                self.resize(10)

        # Removal:
        # Iterate through array to get to index, then shift array to 'remove' element at index and reduce the size
        # to reflect removal of element.
        for i in range(index, self.size - 1, 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1

    def slice(self, start_index: int, size: int) -> object:

        """Returns a new dynamic array object that contains the requested number of elements from the original array
        starting with the element located at the requested start index. If the provided start index or size is
        invalid, or if there are not enough elements between the start index and the end of the array to make the slice
        of the requested size, raises a "DynamicArrayException." """

        # Checks for invalid index and slice:
        if start_index < 0 or start_index >= self.length() or size < 0 or size > self.length()\
                or start_index + size > self.length():
            raise DynamicArrayException

        # Creates a new dynamic array object.
        new_array = DynamicArray()

        # Iterate through the array, starting at the start_index and ending at start_index + size, in order to get
        # the requested slice, appending those elements to the new_array to preserve order.
        for i in range(start_index, start_index + size):
            new_array.append(self.data[i])
        return new_array

    def merge(self, second_da: object) -> None:

        """Takes another dynamic array object as a parameter, and appends all elements from this array onto
        the current one, in the same order as they are stored in the array parameter. Does not return anything."""

        # Iterate through the length of the second_da object using dynamic array length method:
        for i in range(second_da.length()):
            # At each index, call get_at_index method, returning the value from given index position, and appending
            # it to the original array.
            self.append(second_da.get_at_index(i))

    def map(self, map_func) -> object:

        """Creates a new dynamic array where the value of each element is derived by applying a given map_func to
        the corresponding value from the original array. Returns the dynamic array object."""

        # Creates a new dynamic array object.
        new_array = DynamicArray()

        # Iterate through the array to apply the map_func to the elements of the array.
        for i in range(self.length()):
            # Assign the result of the map_func to element.
            element = map_func(self.data[i])
            # Call method to insert the index, value pair in the new array.
            new_array.insert_at_index(i, element)
        # Returns the new dynamic array object.
        return new_array

    def filter(self, filter_func) -> object:

        """Creates a new dynamic array populated only with those elements from the original array for which
        filter_func returns True. Returns the dynamic array object."""

        # Creates a new dynamic array object.
        new_array = DynamicArray()

        # Iterates through the array:
        for i in range(self.length()):
            # If the result of applying the filter_func to an element is True, append that element to the new array.
            if filter_func(self.get_at_index(i)) == True:
                new_array.append(self.get_at_index(i))
        return new_array

    def reduce(self, reduce_func, initializer=None) -> object:

        """Returns the resulting value from applying the reduce_func to all elements of the dynamic array.
        Takes an optional initializer parameter. Condition # 1: If this parameter is not provided, the first value in
        the array is used as the initializer. Condition #2: If the dynamic array is empty, the method returns
        the value of the initializer (or None, if it was not provided). """

        # Condition #2:
        if self.is_empty():
            return initializer

        # Condition #1:
        if initializer == None:
            start_index = 1
            result = self.data[0]
        else:
            start_index = 0
            result = initializer

        # Iterate through the array starting at the 'start index' and applying the reduce_func to the elements.
        for i in range(start_index, self.length()):
            result = reduce_func(result, self.data[i])

        # Return the resulting value from the applying the reduce_func.
        return result

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)


    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")


    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))