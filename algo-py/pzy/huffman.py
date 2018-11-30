class SQueue(object):
    class Node(object):
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def __repr__(self):
            return '<{}>'.format(self.data)

    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.Node(None)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def first(self):
        if self.is_empty():
            raise ValueError('in first')
        return self.head.data

    def _insert_between(self, e, prev_node, next_node):
        #import pdb;pdb.set_trace()
        new_node = self.Node(e, prev_node, next_node)
        new_node.next.prev = new_node
        new_node.prev.next = new_node
        self.size += 1
        return new_node

    def _delete_node(self, node):
        #print(node)
        #import pdb;pdb.set_trace()
        prev_node = node.prev
        next_node = node.next
        prev_node.next = node.next
        next_node.prev = node.prev
        self.size -= 1
        return node.data

    def __repr__(self):
        res = ['HeadSentinal->']
        if not self.is_empty():
            cur = self.head.next
            while cur.next is not None:
                res.append(str(cur.data))
                res.append('->')
                cur = cur.next
        res.append('TailSentinal')
        return ''.join(res)

    def enqueue(self, e):
        self._insert_between(e, self.tail.prev, self.tail)

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty now')
        else:
            return self._delete_node(self.head.next)

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

    #def nr_preorder(self, proc):
    #    ss = SStack()
    #    t = self
    #    while t is not None:
    #        proc(t.data)
    #        if t.right:
    #            ss.push(t.right)

    #        if not t.left:
    #            try:
    #                t = ss.pop()
    #            except ValueError as e:
    #                t = None
    #        else:
    #            t = t.left

    #def nr_postorder(self, proc):
    #    ss = SStack()
    #    t = self
    #    while t is not None or not ss.is_empty():
    #        while t is not None:
    #            ss.push(t)
    #            t = t.left if t.left is not None else t.right
    #        t = ss.pop()
    #        proc(t.data)
    #        if not ss.is_empty() and ss.top().left == t:
    #            t = ss.top().right
    #        else:
    #            t = None

    def order_note(self, trv_mode=0):
        mod_mapping = {
            0: self.preorder,
            1: self.inorder,
            2: self.postorder,
            3: self.levelorder,
            #4: self.nr_preorder,
            #5: self.nr_postorder
        }
        order_num = 0
        def print_proc(data):
            nonlocal order_num
            print("Content={data}, Order={order}".format(
                data=data, order=order_num))
            order_num += 1
        traverse_method = mod_mapping[trv_mode]
        traverse_method(print_proc)

class PrioQueue(object):
    def __init__(self, elist=[]):
        self.element = list(elist)
        if elist:
            self.buildheap()

    def __repr__(self):
        return '-'.join(self.element)

    def is_empty(self):
        return not self.element

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

class HTNode(BinTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data

class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self.element)

def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    print(trees.element)
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
        print(trees.element)
    return trees.dequeue()

if __name__ == "__main__":
    ht = HuffmanTree([2, 2, 7, 10, 4, 3, 5])
    ht.order_note(3)

    #sq = SQueue()
    #for i in range(7):
    #    sq.enqueue(i)
    #print(sq)
    #for i in range(7):
    #    print(sq.dequeue())
    #print(sq)
