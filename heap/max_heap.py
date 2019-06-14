class Heap:
    def __init__(self):
        self.storage = []

    # adds input value to the heap
    # ensure the value is in the correct spot in the heap
    def insert(self, value):
        self.storage.append(value)
        # call bubble up here
        self._bubble_up(len(self.storage) - 1)

    # removes and returns the topmost value from the heap
    # ensure the heap property is maintained after the topmost element has been removed
    def delete(self):
        self.storage[0], self.storage[len(
            self.storage) - 1] = self.storage[len(self.storage) - 1], self.storage[0]
        value_to_return = self.storage.pop()
        self._sift_down(0)
        return value_to_return

    def get_max(self):
        return self.storage[0]

    # returns the number of elements stored in the heap
    def get_size(self):
        return len(self.storage)

    """moves the element at the specified index up the heap
    by swapping it with its parent if the value is less than
    the value at the specified index"""

    def _bubble_up(self, index):
        # keep bubbling up until we've either reached the top of the heap
        # or we've reached a point where the parent is higher priority
        while index > 0:
            # on a single bubble up iteration:
            # get the parent index
            parent = (index - 1) // 2
            # compare the child against the value of the parent
            if self.storage[index] > self.storage[parent]:
                # if the child's value is higher priority than its parents value swap them
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # update the child's index to be the new index it is now at
                index = parent
            # otherwise, child is at a valid spot
            else:
                # stop bubbling up
                break

    """
    Grabs the indices of this elements children and determines which
    child has a larger value. If the larger child's value is larger than
    the parents value, the child element is swapped with the parent.

    Left Child: 2 * index + 1
    Right Child 2 * index + 2
    Parent: (index -1) // 2
    """

    def _sift_down(self, index):
        # check for a left child node
        if (self.get_size() - 1) >= ((2 * index) + 1):
            # if left > index
            if self.storage[(2 * index) + 1] > self.storage[index]:

                # check for a right child node
                if (self.get_size() - 1) >= ((2 * index) + 2):
                    # check if the right node > the left node
                    if self.storage[(2 * index) + 2] > self.storage[(2 * index) + 1]:
                        # if the right > the left swap the right with the index
                        self.storage[(
                            2 * index) + 2], self.storage[index] = self.storage[index], self.storage[(2 * index) + 2]
                        self._sift_down((2 * index) + 2)
                    else:
                        # if the left > the right swap the right with the index
                        self.storage[(
                            2 * index) + 1], self.storage[index] = self.storage[index], self.storage[(2 * index) + 1]
                        # sift to reset the tree
                        self._sift_down((2 * index) + 1)
                else:
                    # The left node is > right node
                    self.storage[(
                        2 * index) + 1], self.storage[index] = self.storage[index], self.storage[(2 * index) + 1]
                    # sift to reset the tree
                    self._sift_down((2 * index) + 1)
            else:
                # check for a right child node
                if (self.get_size() - 1) >= ((2 * index) + 2):
                    # check if the right node < the current node
                    if self.storage[(2 * index) + 2] > self.storage[index]:
                        # if the right > the left swap the right with the index
                        self.storage[(
                            2 * index) + 2], self.storage[index] = self.storage[index], self.storage[(2 * index) + 2]
                        # sift to reset the tree
                        self._sift_down((2 * index) + 2)
