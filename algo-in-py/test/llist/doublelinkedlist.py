class DLNode(object):
    def __init__(
            self, e=None, prev=None, next=None):
        self.element = e
        self.prev = prev
        self.next = next

class DoubleLinkedList(object):
    def __init__(self):
        self.head_sen = DLNode()
        self.tail_sen = DLNode()
        self._size = 0
        self.head_sen.next = self.tail_sen
        self.tail_sen.prev =self.head_sen

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, prev_node, next_node):
        new_node = DLNode(e, prev_node, next_node)
        new_node.next.prev = new_node
        new_node.prev.next = new_node
        self._size += 1
        return new_node

    def _delete_node(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev
        self._size -= 1
        element = n.element
        return element

    def pop_head(self):
        return self._delete_node(
                self.head_sen.next)

    def pop_right(self):
        return self._delete_node(
                self.tail_sen.prev)

    def enque_head(self, e):
        self._insert_between(
            self.head_sen, self.head_sen.next)

    def enque_tail(self, e):
        self._insert_between(
            self.tail_sen.prev, self.tail_sen)
