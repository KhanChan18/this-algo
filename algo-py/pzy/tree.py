class Content(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return '<Key={}:Value={}>'.format(
                self.key, self.value)

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self != other

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

class Node(object):
    def __init__(self, element,
        parent=None, left=None, right=None):

        self.element = element
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return '<Element={}>'.format(self.element)

class Position(object):
    def __init__(self, container, node):
        self.container = container
        self.node = node

    def element(self):
        return self.node.element

    def __eq__(self, other):
        return type(other) is type(self) \
                and other.node is self.node

class Tree(object):
    def _validate(self, p):
        if not isinstance(p, Position):
            raise TypeError(
                'p must be Position type'
            )
        if p.container is not self:
            raise ValueError(
                'p does not belong to this container'
            )
        if p.node.parent is p.node:
            raise ValueError(
                'p is no longer valid'
            )
        return p.node

    def _make_position(self, node):
        return Position(self, node) \
                if node is not None \
                else None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def root(self):
        return self._make_position(self.root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node.parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node.right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            coutn += 1
        return count

    def _add_root(self, p, e):
        node = self._validate(p)
        if self.root is not None:
            raise ValueError('Root exists')

        self.size = 1
        self.root = LBTNode(e)
        return self._make_position(self.root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if self.root is not None:
            raise ValueError('Left exists')
        self.size += 1
        node.left = LBTNode(e, node)
        return self._make_position(node.left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node.right is not None:
            raise ValueError('Right exists')
        self.size += 1
        node.right = LBTNode(e, node)
        return self._make_position(node.right)

    def _replace(self, p, e):
        node = self._validate(p)
        old_value = node.element()
        node.element = e
        return old_value

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError(
                'p has two children'
            )

        child = node.left \
                if node.left else node.right

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
            raise ValueError(
                'position must be leaf'
            )

        if not type(self) is type(t1) is type(t2):
            raise TypeError(
                'Tree types must match'
            )

        self.size += (len(t1) + len(t2))

        if not t1.is_empty():
            t1.root.parent = node
            node.left = t1.root
            t1.root = None
            t1.size = 0

        if not t2.is_empty():
            t2.root.parent = node
            node.right = t2.root
            t2.root = None
            t2.size = 0

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def positions(self):
        return self.inorder()

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def breadthfirst(self):
        if not self.is_empty():
            pass



if __name__ == "__main__":
    chart1 = [c for c in 'abcdefghijklmnopqrstuvwxyz']
    chart2 = [i for i in range(26)]
    dataset = list(zip(chart1, chart2))
    import random
    random.seed(15)
    random.shuffle(dataset)

    for k, v in dataset:
        pass
