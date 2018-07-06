from tree import (
    Content, Node, Position, Tree
)

class TreeMapPosition(Position):
    def key(self):
        return self.element().key

    def value(self):
        return self.element().value

class TreeMap(Tree):
    def _subtree_search(self, p, k):
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(
                    self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(
                        self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        return \
            self._subtree_first_position(self.root()) \
            if len(self) > 0 else None

    def last(self):
        return \
            self._subtree_last_position(self.root()) \
            if len(self) > 0 else None

    def before(self, p):
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(
                    self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None \
                    and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(
                    self.right(p))
        else:
            walk = p
            below = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(
                self.root(), k)
            self._rebalance_access(p)
            return p

    def find_min(self):
        if self.is_empty():
            return None
        else:
            p = self.first()
            return p.key(), p.value()

    def find_ge(self, k):
        if self.is_empty():
            return None:
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value()) \
                    if p is not None else None

    def find_range(self, start, stop):
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None \
                    and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k):



