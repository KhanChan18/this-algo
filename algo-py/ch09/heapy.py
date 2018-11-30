import random

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

class ArrayTreeBase(object):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self.data)

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

    def add(self, e):
        self._data.append(e)

    def preorder(self, j, proc):
        if not self._data:
            return
        proc(self._data[j])
        if self._has_left(j):
            self.preorder(self._left(j), proc)
        if self._has_right(j):
            self.preorder(self._right(j), proc)

    #def levelorder(self, proc):
    #    sq = SQueue()
    #    sq.enqueue(0)
    #    while not sq.is_empty():
    #        j = sq.dequeue()
    #        if n is None:
    #            continue
    #        sq.enqueue(self._left(j))
    #        sq.enqueue(self._right(j))
    #        proc(self._data[j])

    def __repr__(self):
        res = []
        self.preorder(0, res.append)
        return ''.join(str(res))

class HeapPQ(PriorityQueueBase, ArrayTreeBase):
    def __init__(self):
        ArrayTreeBase.__init__()

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

    def add(self, key, value):
        super().add(self._Item(key, value))
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

def randomPair(data):
    data = data.items()
    randomized = random.sample(
            data, len(data))
    print(randomized)
    for d in randomized:
        yield d


if __name__ == "__main__":
    hpq = HeapPQ()
    dataset = {
        6:'C', 4:'A', 5:'Z', 15:'K',
        9:'F', 7:'Q', 20:'B', 16:'X',
        25:'J', 14:'E', 12:'H', 11:'S',
        8:'W'
    }
    for pair in randomPair(dataset):
        hpq.add(*pair)
    hpq.add(2, 'T')
    print(hpq)

