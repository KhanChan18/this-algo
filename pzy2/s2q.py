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

    def first(self):
        if self.is_empty():
            raise ValueError('in first')

        return self.head.element

class SQueue(object):
    READYTOPOP = 'TOPOP'
    READYTOPUSH = 'TOPUSH'
    def __init__(self):
        self.ss_push = SStack()
        self.ss_pop = SStack()
        self.status = SQueue.READYTOPUSH
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        res = []
        if self.ss_push.is_empty():
            if self.ss_pop.is_empty():
                res.append('EmptyQueue')
            else:
                res.append('Head')
                cur = self.ss_pop.head
                while cur.next is not None:
                    res.append('<-{}'.format(cur.element))
                    cur = cur.next
                res.append('<-Tail')
        else:
            res.append('Tail->')
            cur = self.ss_push.head
            while cur.next is not None:
                res.append('{}->'.format(cur.element))
                cur = cur.next
            res.append('Head')
        return ''.join(res)

    def is_empty(self):
        return self.size == 0

    def transform_to_dequeue(self):
        '''Tranform the queue into a popable status
        '''
        if not (self.ss_push.is_empty() \
                and self.ss_pop.is_empty()):
            while not self.ss_push.is_empty():
                e = self.ss_push.pop()
                self.ss_pop.push(e)
        self.status = SQueue.READYTOPOP

    def transform_to_enqueue(self):
        while not self.ss_pop.is_empty():
            e = self.ss_pop.pop()
            self.ss_push.push(e)
        self.status = SQueue.READYTOPUSH

    def enqueue(self, e):
        if self.status is not SQueue.READYTOPUSH:
            self.transform_to_enqueue()
        self.ss_push.push(e)
        self.size += 1

    def dequeue(self):
        if self.status is not SQueue.READYTOPOP:
            self.transform_to_dequeue()
        if self.is_empty():
            raise ValueError('in dequeue')
        e = self.ss_pop.pop()
        self.size -= 1
        return e

if __name__ == "__main__":
    sq = SQueue()
    print(sq)
    for i in range(7):
        sq.enqueue(i)
    print(sq)
    for i in range(3):
        sq.dequeue()
    print(sq)
    for i in range(4):
        sq.enqueue(i)
    print(sq)
    for i in range(5):
        sq.dequeue()
    print(sq)
