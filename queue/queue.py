
from linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    # add item to the back of the queue
    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    # remove and return an item from the front of the queue
    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

    def len(self):
        return self.size
