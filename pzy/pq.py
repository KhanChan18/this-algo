class PQError(ValueError):
    pass

class ListPQ(object):
    def __init__(self, elist=[]):
        self.element = list(elist)
        self.element.sort(reverse=True)

    def enqueue(self, e):
        i = len(self.element) - 1
        while i >= 0:
            if self.element[i] <= e:
                i -= 1
            else:
                break
        self.element.insert(i+1, e)

    def is_empty(self):
        return not self.element

    def peek(self):
        if self.is_empty():
            raise PQError("in top")
        return self.element[-1]

    def dequeue(self):
        if self.is_empty():
            raise PQError("in pop")
        return self.element.pop()

class PrioQueue(object):
    def __init__(self, elist=[]):
        self.element = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self.elements

    def peek(self):
        if self.is_empty():
            raise PQError("in peek")
        return self.element[0]

    def enqueue(self, e):
        self.element.append(None)
        self.siftup(e, len(self.element) - 1)

    def siftup(self, e, last):
        element, i, j = self.element, last, (last - 1) // 2

        while i > 0 and e < element[j]:
            element[i] = element[j]
            i, j = j, (j-1)//2
        element[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PQError("in dequeue")
        element = self.element
        e0 = element[0]
        e = element.pop()

        if len(element) > 0:
            self.siftdown(e, 0, len(element))
        return e0

    def siftdown(self, e, begin, end):
        element, i, j = self.element, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and element[j + 1] < element[j]:
                j += 1
            if e < element[j]:
                break
            element[i] = element[j]
            i, j = j, 2 * j + 1
        element[i] = e

    def buildheap(self):
        end = len(self.element)
        for i in range(end // 2, -1, -1):
            self.siftdown(self.element[i], i, end)
