class Tree(object):
    class Position(object):

        def element(self):
            raise NotImplementedError(
                'Must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError(
                'Must be implemented by subclass')

        def __ne__(self, other):
            raise NotImplementedError(
                'Must be implemented by subclass')

    def root(self):
        raise NotImplementedError(
                'Must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError(
                'Must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError(
                'Must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError(
                'Must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0


class BinaryTree(Tree):

    def left(self, p):
        raise NotImplementedError(
            'Must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError(
            'Must be implemented by subclass')

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

class TreeNode(object):
    def __init__(self, e, parent=None,
            left=None, right=None):
        self.element = e
        self.parent = parent
        self.left = left
        self.right = right

class LinkedBinaryTree(BinaryTree):
    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self.container = container
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return type(other) is type(self) \
                    and other.node is self.node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError(
                'p must be a proper Position type')
        if p.container is not self:
            raise ValueError(
                'p does not belong to this container')
        if p.node.parent is p.node:
            raise ValueError(
                'p is no longer valid')
        return p.node

    def _make_position(self, node):
        return self.Position(self, node) \
                if node is not None else None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

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
        node = self._validate(p)
        return self._make_position(
                node.right)

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

        self.size = 1
        self.root = self.TreeNode(e)
        return self._make_position(self.root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node.left is not None:
            raise ValueError('Left child exists')
        self.size += 1
        node.left = self.TreeNode(e, node)
        return self._make_position(node.left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node.right is not None:
            raise ValueError('Right child exists')
        self.size += 1
        node.left = self.TreeNode(e, node)
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

        child = node.left if node.left else node.right
        if child is not None:
            child.parent = node.parent

        if node is self.root:
            self.root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self.size -= 1
        node.parent = node
        return node.element

    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must e match')
        self.size += (len(t1) + len(t2))

        if not t1.is_empty():
            t1.root.parent = node
            node.left = t1.root
            t1.root = None
            t1.size = 0

        if not t2.is_empty():
            t1.root.parent = node
            node.right = t1.root
            t2.root = None
            t2.size = 0
