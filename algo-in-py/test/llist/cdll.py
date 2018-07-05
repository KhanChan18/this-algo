class DLNode(object):
    def __init__(
            self, e=None, prev=None, next=None):
        self.element = e
        self.prev = prev
        self.next = next

class CircularDoubleLinkedList(object):
    def __init__(self):
        # The next node of sentinal node is the head of whole list
        # The prev node of sentinal node is the tail of whole list
        self.sen = DLNode()
        self.sen.next = self.sen
        self.sen.prev = self.sen
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, prev_node, next_node):
        newnode = DLNode(e, prev_node, next_node)
        newnode.prev.next = newnode
        newnode.next.prev = newnode
        self._size += 1

    def _delete_node(self, n):
        e = n.element
        n.next.prev = n.prev
        n.prev.next = n.next
        self._size -= 1
        return e

    def pop_head(self):


    def push_head(self, e):
