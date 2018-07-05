class TNode(object):
    self __init__(self, e, parent=None
            left=None, right=None):
        self.element = e
        self.parent = parent
        self.left = left
        self.right = right

class TPosition(object):
    def __init__(self, container, node):
        self.container = container
        self.node = node

    def element(self):
        self.node.element

    def __eq__(self, other):
        return type(other) is type(self) \
                and other.node is self.node

    def __ne__(self, other):
        return not self == other

class LBTree(object):

    def _validate(self, p):
        if not isinstance(p, TPosition):
            raise TypeError(
                'p must be a proper Position type.')
        if p.container is not self:
            raise ValueError(
                'p does not belong to this container.')

        if p.node.parent is p.node:
            raise ValueError(
                'p is no longer valid')
        return p.node

    def _make_position(self, node):
        return TPosition(self, node) \
                if node is not None else None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(
                    self.parent(p))

    def height(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(
                self.height(c) \
            for c in self.children(p))

    def root(self):
        return self._make_position(
                self.root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(
                node.parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(
                node.left)

    def right(self, p):
        return self._make_position(
                node.right)

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self.root is not None:
            raise ValueError('Root exists')

        self.size += 1
        node.root = self.TNode(e)
        return self._make_position(self.root)

    def _add_left(self, e, p):
        node = self._validate(p)
        if node.left is not None:
            raise ValueError('Left child exists')

        self.size += 1
        node.left = TNode(e, node)
        return self._make_position(node.left)

    def _add_right(self, e, p):
        node = self._validate(p)
        if node.right is not None:
            raise ValueError('Right child exists')

        self.size += 1
        node.right = TNode(e, node)
        return self._make_position(node.right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node.element
        node.element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError(
                'p has two children')

        child = node.left \
                if node.left else node.right

        if child is not None:
            child.parent = node.parent
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError(
                'Tree types must match each other')
        self.size += (len(t1) + len(t2))

        if not t1.is_empty():
            t1.root.parent = node
            node.left = t1.root
            t1.root = None
            t1.size = 0

        if not t2.is_empty():
            t2.root.parent = node
            node.left = t2.root
            t2.root = None
            t2.size = 0

