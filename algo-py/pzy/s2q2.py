class Node(object):
    def __init__(self, e, next=None):
        self.element = e
        self.next = next

    def __repr__(self):
        return '[{}]'.format(self.element)

class SStack(object):
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        res = []
        if self.is_empty():
            res.append('Empty')
        else:
            cur = self.head
            while cur.next is not None:
                res.append('{}->'.format(cur.element))
                cur = cur.next
            res.append('EndSentinal')
        return ''.join(res)

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = Node(e, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('in pop')
        e = self.head.element
        self.head = self.head.next
        self.size -= 1
        return e

class SQueue(object):
    def __init__(self):
        self.in_stack = SStack()
        self.out_stack = SStack()
        self._size = 0

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        self._size = len(self.in_stack) \
                + len(self.out_stack)

        return self._size

    def __repr__(self):
        res = []
        if self.in_stack.is_empty():
            if self.out_stack.is_empty():
                res.append('EmptyQueue')
            else:
                res.append('Head')
                cur = self.out_stack.head
                while cur.next is not None:
                    res.append('<-{}'.format(cur.element))
                    cur = cur.next
                res.append('<-Tail')
        else:
            res.append('Tail->')
            cur = self.in_stack.head
            while cur.next is not None:
                res.append('{}->'.format(cur.element))
                cur = cur.next
            res.append('Head')
        return ''.join(res)

    def enqueue(self, e):
        self.in_stack.push(e)

    def dequeue(self):
        if self.out_stack.is_empty():
            if self.in_stack.is_empty():
                raise ValueError('EmptyQueue')
            else:
                while not self.in_stack.is_empty():
                    self.out_stack.push(
                        self.in_stack.pop()
                    )
        e = self.out_stack.pop()
        return e

if __name__ == "__main__":
    sq = SQueue()
    for i in range(7):
        sq.enqueue(i)
    print(sq)
    print(sq.in_stack)
    print(sq.out_stack)
    for i in range(3):
        sq.dequeue()
    print(sq)
    print('in stack: ', sq.in_stack)
    print('out stack: ', sq.out_stack)
    for i in range(5):
        sq.enqueue(i)
    print(sq)
    print('in stack', sq.in_stack)
    print('out stack', sq.out_stack)
