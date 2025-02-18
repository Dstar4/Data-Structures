"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        tmp = 0
        if self.length > 0:
            tmp = self.head.value
            if self.head == self.tail:
                self.head = None
                self.tail = None
        else:
            self.head.delete()

        self.length -= 1
        return tmp

    def add_to_tail(self, value):
        if not self.tail:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        tmp = 0
        if self.length > 0:
            tmp = self.tail.value
            if self.tail == self.head:
                self.head = None
                self.tail = None
        else:
            self.tail.delete()

        self.length -= 1
        return tmp

    def move_to_front(self, node):
        if self.head != node:
            node.delete()
        self.head.insert_before(node.value)
        self.head = self.head.prev

    def move_to_end(self, node):
        if self.length > 1 and node != self.tail:
            current_node = node
            node.delete()
        self.tail.insert_after(current_node.value)
        self.tail = self.tail.next
        self.head = self.head if node != self.head else current_node.next

    def delete(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
        if self.length > 0:
            node.delete()
            self.length -= 1

    def get_max(self):
        tmp = self.head
        max_value = tmp.value
        while tmp != self.tail:
            tmp = tmp.next
            if max_value < tmp.value:
                max_value = tmp.value
        return max_value
