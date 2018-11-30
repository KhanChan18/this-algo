import ctypes

class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(
                self._capacity)

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if (k >= self._n) or (k < 0):
            raise IndexError('invalid index')
        return self._A[k]

    def _resize(self, c):
        new_array = self._make_array(c)
        for k in range(len(self._A)):
            new_array[k] = self._A[k]

        self._A = new_array

    def append(self, e):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = e
        self._n += 1

