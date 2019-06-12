"""
Heaps

The point of heaps: Optimal access to priority elements
                                       ^^^^
                                 Max, Min, Longest String
 - Sorting
 - Logging

We want to be able to access the priority element in O(1) time

1. How can I access something in O(1) time?
    -Array indexing (assuming we know the index of what we want to access)
    -By key in a hash table
    -By reference ( the root of a tree )

2. Insert and Delete: the heap still needs to maintain the priority element
    -Insertion: What happens when we insert a new priority element?
    -Deletion: What happens when we delete the priority element?
    - How do we determine the next priority element?

------------------------------------------------------------------------------

DELETION

1. Save a reference to the old priority element so we can return it
2. Overwrite the old priority element with the last element in the array
3. Remove the last element from the array(because we don't want multiple copies)
4. Sift down the element at index 0

-------------------------------------------------------------------------------
"""


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def bubble_up(self, index):
        # keep bubbling up until we've either reached the top of the heap
        # or we've reached a point where the parent is higher priority
        while index > 0:
            parent = (index - 1) // 2
            if self.storate[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[index]
                # update the childs index to be the new index it is now at
                index = parent
            # on a single bubble up iteration:
                # get the parent index
                # compare the child agianst the value of the parent
                # if the child's value is higher priority than its parents value
                # swap them
                # otherwise, child is at a valid spot
                # stop bubbling up

    def _sift_down(self, index):
        pass
