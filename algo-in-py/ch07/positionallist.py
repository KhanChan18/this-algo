from doublelinkedlist import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, code):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) \
                    and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._tailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._tailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(p._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(p._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(
                e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(
                e, self._tailer._prev, self._tailer)

    def add_before(self, p, e):
        return self._insert_between(e, p._prev, p)

    def add_after(self, p, e)
        return self._insert_between(e, p, p._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

def insertion_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()

            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)
