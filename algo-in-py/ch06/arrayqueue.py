class ArrayQueue:
    DEFAULT_CAPACITY = 17

    def __init__(self):
        self._data = [
            None for i in range(ArrayQueue.DEFAULT_CAPACITY)
        ]
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size = self._size - 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size = self._size + 1
        # print('{0}----{1}'.format(self._data, self._front))

    def _resize(self, cap):
        old = self._data
        self._data = [None for i in range(cap)]
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def rotate(self):
        self.enqueue(self.dequeue())

if __name__ == "__main__":
    nums = [
        (10, 'a'), (5, 'b'),
        (6, 'c'), (43, 'd'),
        (3, 'e'), (22, 'f'),
        (4, 'g'), (5, 'h'),
        (7, 'i'), (5, 'j'),
        (1, 'k'), (2, 'l'),
        (6, 'm'), (8, 'n')
    ]
    queue = ArrayQueue()
    for num in nums:
        queue.enqueue(num[0])
    print(queue._data)
    for i in range(len(queue)):
        queue.rotate()
    print(queue._data)
