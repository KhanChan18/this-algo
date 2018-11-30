from s2q2 import SStack

class Content(object):
    def __init__(self, key=None, value=None):
        self.key = None
        self.value = None

class BinTNode(object):
    def __init__(self, element,
            left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

class DictBinTree(object):
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def search(self, k):
        tree = self.root
        while tree is not None:
            if k < tree.element.key:
                tree = tree.left
            if k > tree.element.key:
                tree = tree.right
            else:
                return tree.element.value
        return None

    def insert(self, key, value):
        tree = self.root
        if tree is None:
            self.root = BinTNode(Content(key, value))
        while True:
            if key < tree.element.key:
                if tree.left is None:
                    tree.left = BinTNode(Content(key, value))
                    break
                tree = tree.left
            elif key > tree.element.key:
                if tree.right is None:
                    tree.right = BinTNode(Content(key, value))
                    break
                tree = tree.right
            else:
                tree.element.value = value
                break

    def delete(self, key):
        parent = None
        current = self.root
        while current is not None and current.element.key != key:
            parent = current
            if key < current.element.key:
                current = current.key
            else:
                current = current.right
            if current is None:
                return

        if current.left is None:
            if parent is None:
                self.root = current.right
            elif current is parent.left:
                parent.left = current.right
            else:
                parent.right = current.right
            return

        opc = current.left
        while opc.right is not None:
            current = current.right
        opc.right = current.right
        if parent is None:
            self.root = current.left
        elif parent.left is current:
            parent.left = current.left
        else:
            parent.right = current.left

    def values(self):
        cur = self.root
        ax_stack = SStack()

        while cur is not None or not ax_stack.is_empty():
            while cur is not None:
                ax_stack.push(cur)
                cur = cur.left
            cur = ax_stack.pop()
            yield cur.element.key, cur.element.value
            cur = cur.right

class AVLNode(BinTNode):
    def __init__(self, data):
        BinTNode.__init__(self, data)
        self.bf = 0

class DictAVL(DictBinTree):
    def __init__(self):
        DictBinTree.__init__(self)

    @staticmethod
    def LL(a, b):
        a.left = b.right
        b.right = a
        a.bf = 0
        b.bf = 0
        return b

    @staticmethod
    def RR(a, b):
        a.right = b.left
        b.left = a
        a.bf = 0
        b.bf = 0
        return b

    @staticmethod
    def LR(a, b):
        c = b.right
        a.left = c.right
        b.right = c.left
        c.left = b
        c.right = a

        if c.bf == 0:
            a.bf = 0
            b.bf = 0
        elif c.bf == 1:
            a.bf = 1
            b.bf = 0
        else:
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    @staticmethod
    def RL(a, b):
        c = b.left
        a.right = c.left
        b.left = c.right
        c.left = a
        c.right = b

        if c.bf == 0:
            a.bf = 0
            b.bf = 0
        elif c.bf == 1:
            a.bf = 0
            b.bf = -1
        else:
            a.bf = 1
            b.bf = 0
        c.bf = 0
        return c

    def insert(self, key, value):
        a = self.root
        p = self.root
        if a is None:
            self.root = AVLNode(Content(key, value))
            return
        pa = None
        q = None
        while p is not None:
            if key == p.element.key:
                p.element.value = value
                return
            if p.bf != 0:
                pa, a = q, p
            q = p
            if key < p.element.key:
                p = p.left
            else:
                p = p.right

        node = AVLNode(Content(key, value))
        if key < q.element.key:
            q.left = node
        else:
            q.right = node

        if key < a.element.key:
            p = a.left
            b = a.left
            d = 1
        else:
            p = a.right
            b = a.right
            d = -1

        while p != node:
            if key < p.element.key:
                p.bf = 1
                p = p.left
            else:
                p.bf = -1
                p = p.right

        if a.bf == 0:
            a.bf = d
            return
        if a.bf == -d:
            a.bf = 0
            return

        if d == 1:
            if b.bf == 1:
                b = DictAVL.LL(a, b)
            else:
                b = DictAVL.LR(a, b)
        else:
            if b.bf == -1:
                b = DictAVL.RR(a, b)
            else:
                b = DictAVL.RL(a, b)

        if pa is None:
            self.root = b
        else:
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b
