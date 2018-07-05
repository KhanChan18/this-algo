class LinkedListError(ValueError):
    pass

class LinkedStackError(
        LinkedListError):
    pass

class LinkedQueueError(
        LinkedListError):
    pass

class SNode(object):
    def __init__(self, element, next):
        self.element = element
        self.next = next

class DNode(SNode):
    def __init__(self, element, prev, next):
        super.__init__(element, next)
        self.prev = prev

class LinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def prepend(self, e):
        self._head = SNode(e, self._head)
        if self.is_empty():
            self._tail = new_node
        self._size += 1

    def append(self, e):
        new_node = SNode(e, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise LinkedListError("in pop proc of LinkedList")
        e = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self._head is None:
            self._tail = None
        return e

    def pop_last(self):
        if self.is_empty():
            raise LinkedListError("in pop_last proc of LinkedList")
        cur = self._head
        if cur.next is None:
            e = cur.element
            self._head = None
        else:
            while cur.next is not None:
                cur = cur.next
            e = cur.next.element
            cur.next = None
            self._tail = cur
        return e

class LinkedStack(object):
    def __init__(self):
        self._size = 0
        self._head = None

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise LinkedListError("Stack is empty")
        return self._head.element

    def push(self, e):
        self._head = SNode(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise LinkedStackError("Stack is empty.")
        e = self._head.element
        self._head = self._head.next
        self._size -= 1
        return e

class LinkedQueue(object):
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def enqueue(self, e):
        new_node = SNode(e, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise LinkedQueueError("Queue is empty.")
        e = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return e

class CircularLinkedQueue(object):
    def __init__(self):
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def enqueue(self, e):
        new_node = SNode(e, None)
        if self.is_empty():
            new_node.next = new_node
        else:
            new_node.next = self._tail.next
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise LinkedQueueError("Queue is empty.")

        oldhead = self._tail.next
        if self._size == 1:
            self._tail = None
        else:
            sefl._tail.next = oldhead.next
        self._size -= 1
        return oldhead.element

