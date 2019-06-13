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
        pass

    def get_priority(self):
        pass

    # returns the number of elements stored in the heap
    def get_size(self):
        pass

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

    """grabs the indices of this elements children and determines which
    child has a larger value. If the larger child's value is larger than
    the parents value, the child element is swapped with the parent."""

    def _sift_down(self, index):
        pass
