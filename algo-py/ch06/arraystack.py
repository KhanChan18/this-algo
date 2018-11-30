class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

if __name__ == "__main__":
    ele = ArrayStack()
    import pdb;pdb.set_trace()
