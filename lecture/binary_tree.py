
"""
Binary Search Tree(BST) Data Structure
---------------------------------
Data does not need to be sorted
Provides order to unsorted data

-------------------------------------------------------

1. Compare the element against the current node's value
2. Based on the result of step 1, go left or right
3. If we find and empty spot, park the value there
4. Otherwise, go back to step 1.

-------------------------------------------------------

 __________________________
|      | Insert   | Search |
|BST   | O(log n) | O(log n)|
|Array | O(1)     | O(n)   |
 --------------------------


Properties of a Binary Search Tree
--------------------------------------------------------

-The left subtree of a node contains only nodes with keys lesser than the node’s key.
-The right subtree of a node contains only nodes with keys greater than the node’s key.
-The left and right subtree each must also be a binary search tree (recursive).

Searching a key
-------------------------------------------------------
-To search a given key in Binary Search Tree, we first compare it with root,
 if the key is present at root, we return root. If key is greater than root’s key,
 we recur for right subtree of root node.
-Otherwise we recur for left subtree.

"""


class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:

            # if value is less we go left
            # if there is no left child, we can park this node here

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

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
