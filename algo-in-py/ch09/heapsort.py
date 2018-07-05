class _DoublyLinkedBase(object):
    class _Node(object):
        def __init__(self, element,
                prev=None, next=None):
            self.element = element
            self.prev = prev
            self.next = next

        def __repr__(self):
            return '[{}]'.format(self.element)

    def __init__(self):
        self.header = self._Node(None)
        self.tailer = self._Node(None)
        self.size = 0

        self.header.next = self.tailer
        self.tailer.prev = self.header

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _insert_between(self, e,
            prev_node, next_node):
        new_node = self._Node(e, prev_node, next_node)
        prev_node.next = new_node
        next_node.prev = new_node
        self.size += 1
        return new_node

    def _delete_node(self, node):
        e = node.element
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return e

    def __repr__(self):
        res = ['HeadSentinal', '->']
        if not self.is_empty():
            cur = self.header.next
            while cur.next.next is not None:
                res.append(cur.element)
                res.append('->')
                cur = cur.next
        res.append('TailSentinal')
        return ''.join(res)

class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return type(other) is type(self) \
                    and other.node is self.node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError(
                'p must be proper Position type')

        if p.container is not self:
            raise ValueError(
                'p does not belong to this container')

        if p.node.next is None:
            raise ValueError('p is no longer valid')
        return p.node

    def _make_position(self, node):
        if node is self.header \
            or node is self.tailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self.header.next)

    def last(self):
        return self._make_position(self.tailer.prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(p.prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(p.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e,
            predecessor, successor):
        node = super()._insert_between(
                e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(
                e, self.header, self.header.next)

    def add_last(self, e):
        return self._insert_between(
                e, self.tailer.prev, self.tailer)

    def add_before(self, p, e):
        return self._insert_between(e, p.prev, p)

    def add_after(self, p, e):
        return self._insert_between(e, p, p.next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original.element
        original.element = e
        return old_value

class PriorityQueueBase:
    class _Item:
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

        def __repr__(self):
            return '<{}:{}>'.format(self._key, self._value)

    def is_empty(self):
        return len(self) == 0

class HeapPQ(PriorityQueueBase):
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = \
            self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left

            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right

            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        res = []
        for d in self._data:
            res.append(d.__repr__())
        return ''.join(res)

    def add(self, key, value):
        self._data.append(
            self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError('PQ is empty')

        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError('PQ is empty')

        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

def pq_sort(C):
    n = len(C)
    P = HeapPQ()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)
    for j in range(n):
        (k, v) = P.remove_min()
        C.add_last(v)

if __name__ == "__main__":
    import random
    import string
    samples = string.ascii_uppercase

    C = PositionalList()
    import pdb;pdb.set_trace()
    dataset = [
        ''.join(random.choice(samples) \
                for i in range(8)) for i in range(20)
    ]
    print(dataset)
    for d in dataset:
        C.add_last(d)
    print(C)
    pq_sort(C)
    print(C)
