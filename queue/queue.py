class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    # adds item to the back of the que
    def enqueue(self, item):
        pass

    # remove and return an item from the front of the que
    def dequeue(self):
        self.storage = self.storage.pop(0)

    # returns the number of items in the que
    def len(self):
        pass
