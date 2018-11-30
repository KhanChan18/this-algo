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
            if walk.
