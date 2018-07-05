left_parens = "([{<"
parens_mappings = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


class LinkedStackError(ValueError):
    def __init__(self, msg=None):
        if msg is None:
            msg = 'Stack is empty.'
        super.__init__(msg)

class Node(object):
    def __init__(self, e, next):
        self.element = e
        self.next = next

class LinkedStack(object):
    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise LinkedStackError()
        return self.head.element

    def push(self, e):
        self.head = Node(e, self.head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise LinkedStackError()
        e = self.head.element
        self.head = self.head.next
        self._size -= 1
        return e

def is_parens_balance(testset):
    st = LinkedStack()
    for pr in testset:
        if pr not in '([{<>}])':
            continue
        elif pr in left_parens:
            st.push(pr)
        elif st.pop() != parens_mappings[pr]:
            return False
    return True

if __name__ == "__main__":
    document = '''
    (c436071a-(7b47-11e8-a695-080027efde53
    c436071b-7b47-11e8-a695-080027efde53
    c4)36071c-7[b47-11e8-a695<-080027efde53
    c436071d-7b47-11e8-a695-080027efde53
    c436>071e-7b4]7-11e8-a{695-08[0027efde53
    c436071f<-7b47-11e8-a695-08002>7efde53
    c436072]0-7b47-11e8-a}695-080027efde53)
    '''
    print is_parens_balance(document)
