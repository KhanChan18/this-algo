class LinkedStackError(Exception):
    def __init__(self, msg=None, **kwargs):
        if msg is None:
            msg = 'Stack is empty'
        super(LinkedStackError, self).__init__(
                msg)

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

    def printall(self):
        cur = self.head
        msg_str = ['[']
        while cur is not None:
            msg_str.append(str(cur.element))
            msg_str.append(',')
            cur = cur.next
        msg_str.append(']')
        print ''.join(msg_str)

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

op_mappings = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x*y,
    "/": lambda x, y: x/y
}


def suf_exp_evaluator(exp):
    exp = exp.split()
    print exp
    operators = "+-*/"
    st = LinkedStack()
    st.printall()
    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue

        if len(st) < 2:
            raise SyntexError("Short of operands.")
        a = st.pop()
        b = st.pop()
        c = op_mappings[x](b, a)
        st.push(c)
        st.printall()

    if len(st) == 1:
        return st.pop()
    else:
        raise SyntexError("Extra operands founded")

def trans_infix_suffix(line):
    infix_operators = '+-*/()'
    priority = {
        "(": 1,
        "+": 3, "-": 3,
        "*": 5, "/": 5
    }

    st = LinkedStack()
    exp = []

    for x in tokens(line):
        if x not in infix_operators:
            exp.append(x)
        elif st.is_empty() or x == '(':
            st.push(x)
        elif x == ')':
            while not st.is_empty() and st.first() != '(':
                exp.append(st.pop())
            if st.is_empty():
                raise SyntexError('Missing \' ( \'')
            st.pop()
        else:
            while (not self.is_empty() and
                    priority[st.first()] >= priority[x]):
                exp.append(st.pop())
            st.push(x)

    while not st.is_empty():
        if st.first() == '(':
            raise SyntaxError("Extra '('")
        exp.append(st.pop())
    return exp

def infix_evaluator(expression):
    exps = expression.split(' ')
    st_operand = LinkedStack()
    st_operator = LinkedStack()

    for exp in exps:
        st_operand.printall()
        st_operator.printall()
        if exp == '(' or exp in op_mappings:
            st_operator.push(exp)
            # continue
        elif exp not in '+-*/()':
            st_operand.push(float(exp))
        elif exp == ')':
            try:
                while st_operator.first() is not '(':
                    a = st_operand.pop()
                    b = st_operand.pop()
                    st_operand.push(
                        op_mappings[st_operator.pop()](b, a))
                st_operator.pop()
            except LinkedStackError() as e:
                print "Errors happend: {}".format(e)

    return st_operand.pop()

if __name__ == "__main__":
    # print suf_exp_evaluator('3 5 - 6 17 4 * + * 3 /')
    print infix_evaluator('( ( 3 - 5 ) * ( 6 + 17 * 4 ) / 3 )')
