class LinkedListUnderflow(ValueError):
    pass

class LNode:
    def __init__(self, e, next_=None):
        self.element = e
        self.next = next_

class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, e):
        self._head = LNode(e, self._head)

    def pop(self):
        if self.is_empty():
            raise LinkedListUnderflow('in pop')
        e = self._head.element
        self._head = self._head.next
        return e

    def append(self, e):
        if self._head is None:
            self._head = LNode(e)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(e)

    def pop_last(self):
        if self.is_empty():
            raise LinkedListUnderflow('in pop_last')
        p = self._head
        if p.next is None:
            e = p.element
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.element
        p.next = None
        return e

    def find(self, func):
        p = self._head
        while p is not None:
            if func(p.element):
                return p.element
            p = p.next

    def for_each(self, func):
        p = self._head
        while p is not None:
            func(p.element)
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.element
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.element, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')

    def gen_from_list(self, lst):
        if hasattr(lst, '__next__'):
            lst = list(lst)
        cur = self._head
        while cur.next is not None:
            cur = cur.next

        for e in lst:
            cur.next = LNode(e)
            cur = cur.next

class LList1(LList):
    def __init__(self):
        super.__init__(self)
        self._rear = None

    def prepend(self, e):
        if self.is_empty():
            self._head = LNode(e, self._head)
            self._rear = self._head
        else:
            self._head = LNode(e, self._head)

    def append(self, e):
        if self.is_empty():
            self._head = LNode(e, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(e)
            self._rear = self._rear.next

    def pop_last(self):
        if self.is_empty():
            raise LinkedListUnderflow('in pop last')
        cur = self._head
        if cur.next is None:
            e = cur.element
            self._head = None
            return e
        while cur.next.next is not None:
            cur = cur.next
        e = cur.next.element
        cur.next = None
        self._rear = cur
        return e

class LClist:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, e):
        p = LNode(e)
        if self.is_empty():
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, e):
        self.prepend(e)
        self._rear = self._rear.next

    def pop(self):
        if self.is_empty():
            raise LinkedListUnderflow('in pop')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.element

class DLNode(LNode):
    def __init__(self, e, prev=None, next=None):
        super.__init__(self, e, next)
        self.prev = prev

class DLList(LList1):
    def __init__(self):
        super.__init__(self)

    def prepend(self, e):
        p = DLNode(e, None, self._head)
        if self.is_empty():
            self._rear = p
        else:
            p.next.prev = p
        self._head = p



if __name__ == "__main__":
    ll = LList()
    for i in range(5):
        ll.append(i)
    ll.printall()
    ll.gen_from_list([i for i in range(30) if i % 3 == 1])
    ll.gen_from_list(i for i in range(30) if i % 2 == 1)
    ll.printall()
