from positionallist import PositionalList

class PriorityQueueBase:
    class _Item:
        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __lt__(self, other):
            return self.key < other.key

    def is_empty(self):
        return len(self) == 0

class UnsortedPriorityQueue(PriorityQueueBase):
    def _find_min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')

        small = self.data.first()
        walk = self.data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self.data.after(walk)
        return small

    def __init__(self):
        self.data = PositionalList()

    def __len__(self):
        return len(self.data)

    def add(self, key, value):
        self.data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self.data.delete(p)
        return (item.key, item.value)
