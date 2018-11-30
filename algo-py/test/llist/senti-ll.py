class LNode(object):
    def __init__(self, e=None, next=None):
        self.element = element
        self.next = next

class SentinalLinkedList(object):
    def __init__(self):
        self.tail = LNode(None, None)
        self.head = LNode(None, self.tail)
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def pop(self):
        if self.is_empty():
            raise Exception()
        e = self.head.next.element
        self.head.next = self.head.next.next
        self._size -= 1

    def push(self, e):
        self.head.next = LNode(e, self.head.next)
        self._size += 1
