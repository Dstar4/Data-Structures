class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #  adds the input value to the binary search tree
    def insert(self, value):
        # if value is less we go left
        # if there is no left child, we can park this node here
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)

        # recurse on the left child
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # searches tree for the input value, returning a boolean if it exists or not
    def contains(self, target):
        # use a while loop to check self.values against target - if it finds a match return True
        while True:
            # check if the target is equal to the current node
            if target == self.value:
                return True
            # check if target is less than the node value and that a left node exists
            elif target < self.value and self.left:
                # set self to the new node down the tree
                self = self.left

            #  if target is > self.value and a right node exists
            elif target > self.value and self.right:
                # set self to the new node down the tree
                self = self.right

            # if no match is found return False
            else:
                return False
        # returns the maximum value in the binary search tree

    def get_max(self):
        pass

    # performs a traversal of every node, executing the cb on every tree node value
    def for_each(self, cb):
        pass
