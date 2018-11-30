class SQueue(object):
    class SQNode(object):
        def __init__(self, e,
                prev=None, next=None,
                desc=None):
            self.element = e
            self.prev = prev
            self.next = next
            self.desc = desc

        def __repr__(self):
            return '[Content: {}, Description: {}]'.format(
                    self.element, self.desc)

    def __init__(self):
        self.head = self.SQNode(None)
        self.tail = self.SQNode(None)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size is 0

    def first(self):
        if self.is_empty():
            raise ValueError('in first')
        print(self.head.next)

    def _insert_between(self, e, prev_node, next_node, desc=None):
        new_node = self.SQNode(e, prev_node, next_node, desc)
        new_node.prev.next = new_node
        new_node.next.prev = new_node
        self.size += 1
        return new_node

    def _delete_node(self, node):
        e = node.element
        res_node = node
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return res_node

    def enqueue(self, e, desc):
        self._insert_between(
            e, self.tail.prev, self.tail, desc)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("in dequeue")
        return self._delete_node(self.head.next)

class SStack(object):
    class SSNode(object):
        def __init__(self, e, next=None):
            self.element = e
            self.next = next

    def __init__(self):
        self.head = self.SSNode(None)
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def top(self):
        if self.is_empty():
            raise ValueError('in first')
        return self.head.element

    def push(self, e):
        self.head = self.SSNode(e, self.head)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('in pop')
        e = self.head.element
        self.head = self.head.next
        self.size -= 1
        return e

class Node(object):
    def __init__(self, element,
            left=None, right=None):
        self.key = element[0]
        self.value = element[1]
        self.left = left
        self.right = right

    def __repr__(self):
        return '<{0}:{1}>'.format(self.key, self.value)


class BinTreeDict(object):
    def __init__(self, tree=None):
        self.root = tree

    def is_empty(self):
        return self.root is None

    def printdict(self):
        i = 0
        for k, v in self.values():
            print('Content: {0}, Order: {1}'.format((k, v), i))
            i = i + 1

    def search(self, targ):
        if self.is_empty():
            raise ValueError('in search')
        cur = self.root
        while cur is not None:
            if targ == cur.key:
                return cur.value
            elif targ < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def insert(self, key, value):
        cur = self.root
        if cur is None:
            self.root = Node((key, value))
            return
        while True:
            #print("cur: {}".format(cur))
            if key < cur.key:
                if cur.left is None:
                    cur.left = Node((key, value))
                    return
                cur = cur.left
            elif key > cur.key:
                if cur.right is None:
                    cur.right = Node((key, value))
                    return
                cur = cur.right
            else:
                cur.value = value
                return

    def values(self):
        ss = SStack()
        cur = self.root
        while cur is not None or not ss.is_empty():
            while cur is not None:
                ss.push(cur)
                cur = cur.left
            cur = ss.pop()
            yield (cur.key, cur.value)
            cur = cur.right

    def post_values(self):
        ss = SStack()
        cur = self.root
        while cur is not None or ss.is_empty():
            while cur is not None:
                print(cur.key, cur.value)
                if cur.right is not None:
                    ss.push(cur.right)
                cur = cur.left
            if not ss.is_empty():
                cur = ss.pop()
            else:
                break

    def delete(self, k):
        p = None
        q = self.root
        while q is not None and q.key != k:
            p = q
            if k < q.key:
                q = q.left
            else:
                q = q.right
            if q is None:
                return

        if q.left is None:
            if p is None:
                self.root = q.right
            elif p.left is q:
                p.left = q.right
            else:
                p.right = q.right
            return

        r = q.left
        while r.right is not None:
            r = r.right
        r.right = q.right
        if p is None:
            self.root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

def reg_to_res(key, value, res):
    if key in res:
        res[key].append(value)
    else:
        res[key] = [value]

def levelprint(tree):
    if tree is None:
        print('EmptyTree')
    else:
        res = {}
        sq = SQueue()
        sq.enqueue(tree, 1)
        while not sq.is_empty():
            sqn = sq.dequeue()
            cur = sqn.element
            cur_lvl = sqn.desc
            if cur is None:
                continue
            sq.enqueue(cur.left, cur_lvl+1)
            sq.enqueue(cur.right, cur_lvl+1)
            reg_to_res(cur_lvl, str(cur), res)

        for k, v in res.items():
            output = \
                    '{lvl}:{content}'.format(lvl=k ,content=v)
            print(output)

if __name__ == "__main__":
    btd = BinTreeDict()
    chart1 = [c for c in 'abcdefghijklmnopqrstuvwxyz']
    chart2 = [i for i in range(26)]
    import random
    dataset = list(
        zip(chart1, chart2)
    )
    random.shuffle(dataset)
    for k, v in dataset:
        #print(k, v)
        btd.insert(k, v)
    btd.printdict()
    levelprint(btd.root)
    deprecated_keys = [c for c in chart1 if ord(c) % 3 == 2]
    print(deprecated_keys)
    for k in deprecated_keys:
        btd.delete(k)

    for c in deprecated_keys:
        print(btd.search(c))
    btd.printdict()
