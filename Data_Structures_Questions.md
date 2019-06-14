Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
O(n)
2. What is the runtime complexity of `dequeue`?
O(1)
3. What is the runtime complexity of `len`?
O(n)
## Binary Search Tree

1. What is the runtime complexity of `insert`?

The runtime of insert will depend on the height of the tree
In the worst case it could be O(n) but in general it will be O(h) where h is the height of the tree.

2. What is the runtime complexity of `contains`?

The runtime for contains will be similar to insert, because they will have to traverse the tree in a similar manner.
O(n) worst case
O(h) average case

3. What is the runtime complexity of `get_max`?
O(h) where h is the height of the tree.


## Heap

1. What is the runtime complexity of `_bubble_up`?
O(log n)
2. What is the runtime complexity of `_sift_down`?
O(log n)
3. What is the runtime complexity of `insert`?
O(log n)
4. What is the runtime complexity of `delete`?
O(log n)
5. What is the runtime complexity of `get_max`?
O(1)
## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
O(n)
2. What is the runtime complexity of `ListNode.insert_before`?
O(n)
3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(n)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(n)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(n)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(n)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    The delete method has a O(1) runtime where an array splice has an O(n) runtime. Although if you include the movement the delete takes to get to the desired node, it also is O(n) so overall they are about the same.
