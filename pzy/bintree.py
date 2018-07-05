class BinTNode(object):
    def __init__(self, data,
        left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return 'data={}'.format(self.data)

    def preorder(self, proc):
        if self is None:
            return
        proc(self.data)
        if self.left:
            self.left.preorder(proc)
        if self.right:
            self.right.preorder(proc)

    def inorder(self, proc):
        if self is None:
            return
        if self.left:
            self.left.inorder(proc)
        proc(self.data)
        if self.right:
            self.right.inorder(proc)

    def postorder(self, proc):
        if self is None:
            return
        if self.left:
            self.left.postorder(proc)
        if self.right:
            self.right.postorder(proc)
        proc(self.data)

    def levelorder(self, proc):
        sq = SQueue()
        sq.enqueue(self)
        while not sq.is_empty():
            n = sq.dequeue()
            if n is None:
                continue
            sq.enqueue(n.left)
            sq.enqueue(n.right)
            proc(n.data)

    def nr_preorder(self, proc):
        ss = SStack()
        t = self
        while t is not None:
            proc(t.data)
            if t.right:
                ss.push(t.right)

            if not t.left:
                try:
                    t = ss.pop()
                except ValueError as e:
                    t = None
            else:
                t = t.left

    def nr_postorder(self, proc):
        ss = SStack()
        t = self
        while t is not None or not ss.is_empty():
            while t is not None:
                ss.push(t)
                t = t.left if t.left is not None else t.right
            t = ss.pop()
            proc(t.data)
            if not ss.is_empty() and ss.top().left == t:
                t = ss.top().right
            else:
                t = None

    def order_note(self, trv_mode=0):
        mod_mapping = {
            0: self.preorder,
            1: self.inorder,
            2: self.postorder,
            3: self.levelorder,
            4: self.nr_preorder,
            5: self.nr_postorder
        }
        order_num = 0
        def print_proc(data):
            nonlocal order_num
            print("Content={data}, Order={order}".format(
                data=data, order=order_num))
            order_num += 1
        traverse_method = mod_mapping[trv_mode]
        traverse_method(print_proc)

class SQueue(object):

    class Node(object):
        def __init__(self, data, prev, next):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def first(self):
        if self.is_empty():
            raise ValueError('in first')
        return self.head.next.element

    def last(self):
        if self.is_empty():
            raise ValueError('in last')
        return self.tail.prev.element

    def _insert_between(self, e, prev_node, next_node):
        new_node = self.Node(e, prev_node, next_node)
        prev_node.next = new_node
        next_node.prev = new_node
        self.size += 1
        return new_node

    def _delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = node.next
        next_node.prev = node.prev
        self.size -= 1
        return node.data

    def enqueue(self, e):
        self._insert_between(e, self.tail.prev, self.tail)

    def enqueue_head(self, e):
        self._insert_between(e, self.head, self.head.next)

    def dequeue(self):
        if self.is_empty():
            raise ValueError('in dequeue')
        return self._delete_node(self.head.next)

    def dequeue_last(self):
        if self.is_empty():
            raise ValueError('in dequeue last')
        return self._delete_node(self.tail.prev)

    def printQ(self):
        print(self)

    def __repr__(self):
        result = ''
        if self.is_empty():
            result = 'HeadSential->TailSential'
        else:
            contents = ['HeadSentinal->']
            cur = self.head.next
            while cur.next is not None:
                contents.append('{}->'.format(cur.data))
                cur = cur.next
            contents.append('TailSentinal')
            result = ''.join(contents)
        return result

class SStack(object):
    class Node(object):
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = self.Node(None, None)
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def push(self, e):
        self.head = self.Node(e, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('in pop')
        e = self.head.data
        self.head = self.head.next
        self.size -= 1
        return e

    def __repr__(self):
        result = ''
        if self.is_empty():
            result = 'TailSential'
        else:
            contents = []
            cur = self.head
            while cur.next is not None:
                contents.append('{}->'.format(cur.data))
                cur = cur.next
            contents.append('TailSentinal')
            result = ''.join(contents)
        return result

def bt_search(btree, key):
    bt = btree
    while bt is not None:
        entry = bt.data
        if key < entry:
            bt = bt.left
        elif key > entry:
            bt = bt.right
        else:
            return entry
    return None

if __name__ == "__main__":
    #tree = BinTNode(
    #    57,
    #    BinTNode(
    #        36,
    #        BinTNode(7, BinTNode(2), BinTNode(18)),
    #        BinTNode(43, BinTNode(40), BinTNode(52))
    #    ),
    #    BinTNode(
    #        89,
    #        BinTNode(65, BinTNode(60), BinTNode(74)),
    #        BinTNode(96, BinTNode(98), BinTNode(103))
    #    )
    #)
    tree = BinTNode(
        65,
        BinTNode(
            7,
            None,
            BinTNode(
                43,
                BinTNode(36, BinTNode(18), None),
                BinTNode(57, BinTNode(52), BinTNode(60)))
        ),
        BinTNode(
            96,
            BinTNode(74, None, BinTNode(89)),
            None
        )
    )

    print('Pre-root order')
    tree.order_note(0)
    print('Non-Recursive Pre-root order')
    tree.order_note(4)
    print('Breadth-first order')
    tree.order_note(3)
    print('Recursive In-root order')
    tree.order_note(1)
    print('Recursive Post-root order')
    tree.order_note(2)
    print('Non-Recursive Post-root order')
    tree.order_note(5)

    search_list = [96, 89, 74]
    for item in search_list:
        print(bt_search(tree, item))
