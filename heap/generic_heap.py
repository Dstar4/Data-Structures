class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator

    # adds input value to the heap
    # ensure the value is in the correct spot in the heap
    def insert(self, value):
        self.storage.append(value)

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
        pass

    """grabs the indices of this elements children and determines which
    child has a larger value. If the larger childs value is larger than
    the parents value, the child element is swapped with the parent."""

    def _sift_down(self, index):
        pass
