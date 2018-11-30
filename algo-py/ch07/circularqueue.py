class CircularQueue:
    class _Node:
        __slots__ == '_next', '_element'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next

        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newnode = self._Node(e, None)
        if self.is_empty():
            newnode._next = newnode
        else:
            newnode._next = self._tail._next
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1

    def rotate(self):
        if not self.is_empty():
            self._tail = self._tail._next


